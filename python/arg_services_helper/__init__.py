import contextlib
import multiprocessing
import socket
import traceback
import typing as t
from concurrent import futures
from operator import attrgetter

import grpc


def handle_except(ex: Exception, ctx: grpc.ServicerContext) -> None:
    """Handler that can be called when handling an exception.

    It will pass the traceback to the gRPC client and abort the context.

    Args:
        ex: Exception that occured.
        ctx: Current gRPC context.
    """

    msg = "".join(traceback.TracebackException.from_exception(ex).format())
    ctx.abort(grpc.StatusCode.UNKNOWN, msg)


def require(
    attrs: t.Collection[str],
    obj: object,
    ctx: grpc.ServicerContext,
    parent: t.Optional[str] = None,
) -> None:
    """Verify that all required arguments are supplied by the client.

    If arguments are missing, the context will be aborted

    Args:
        attrs: Names of the required parameters.
        obj: Current request message (e.g., a subclass of google.protobuf.message.Message).
        ctx: Current gRPC context.
        parent: Name of the parent message. Only used to compose more helpful error.
    """
    if not parent:
        parent = "request"

    func = attrgetter(*attrs)
    attr_result = func(obj)

    if len(attrs) == 1:
        attr_result = [attr_result]

    if not all(attr_result):
        ctx.abort(
            grpc.StatusCode.INVALID_ARGUMENT,
            f"The message '{parent}' requires the following attributes: {attrs}.",
        )


def _serve_single(
    bind_address: str,
    add_services: t.Callable[[grpc.Server], None],
    threads: int,
    reuse_port: bool,
):
    """Helper function to start a server for a single process.

    Args:
        bind_address: Complete address consisting of hostname and port (e.g., `127.0.0.1:8000`)
        add_services: Function to inject the gRPC services into the server instance.
        threads: Number of workers per process.
        reuse_port: If using multiple processes, the port has to be reused.
    """

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=threads),
        options=(("grpc.so_reuseport", 1 if reuse_port else 0),),
    )
    add_services(server)

    server.add_insecure_port(bind_address)
    server.start()
    server.wait_for_termination()


def serve(
    host: str,
    port: int,
    add_services: t.Callable[[grpc.Server], None],
    processes: int = 1,
    threads: int = 1,
):
    """Serve one or multiple gRPC services, optionally using multiprocessing.

    Args:
        host: Hostname of the server (e.g., `127.0.0.1`)
        port: Port of the server. Use `0` to let the server determine an open port.
        add_services: Function to inject the gRPC services into the server instance.
        processes: If `processes > 1`, multiprocessing with a reused port is applied.
        threads: Number of workers per process.

    Raises:
        ValueError: If `processes < 0` is given.
    """

    if processes < 0:
        raise ValueError("No negative number of processes allowed.")

    reuse_port = processes > 1

    with _reserve_port(port, reuse_port) as actual_port:
        bind_address = f"{host}:{actual_port}"
        print(f"Serving on {bind_address}")
        args = (bind_address, add_services, threads, reuse_port)

        if processes == 1:
            _serve_single(*args)
        else:
            workers = []

            for _ in range(processes):
                worker = multiprocessing.Process(target=_serve_single, args=args)
                worker.start()
                workers.append(worker)

            for worker in workers:
                worker.join()


@contextlib.contextmanager
def _reserve_port(
    port: int = 0, reuse_port: bool = False
) -> t.Generator[int, None, None]:
    """Find and reserve a port for all subprocesses to use.

    Args:
        port: Desired port. If `0`, the method will automatically determine a free port.
        reuse_port: If using multiple processes, set this to `True`.
            Only affects multiprocessing, not multithreading.

    Yields:
        Port that has been reserved

    Raises:
        RuntimeError: If the port could not be reused
    """

    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

    if reuse_port:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        if sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT) == 0:
            raise RuntimeError("Failed to set SO_REUSEPORT.")

    sock.bind(("", port))

    try:
        yield sock.getsockname()[1]
    finally:
        sock.close()
