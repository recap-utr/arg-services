import multiprocessing as mp
import traceback
import typing as t
from concurrent import futures
from operator import attrgetter

import grpc
from grpc_reflection.v1alpha import reflection


def handle_except(ex: Exception, ctx: grpc.ServicerContext) -> None:
    """Handler that can be called when handling an exception.

    It will pass the traceback to the gRPC client and abort the context.

    Args:
        ex: Exception that occured.
        ctx: Current gRPC context.
    """

    msg = "".join(traceback.TracebackException.from_exception(ex).format())
    ctx.abort(grpc.StatusCode.UNKNOWN, msg)


def require_any(
    attrs: t.Collection[str],
    obj: object,
    ctx: grpc.ServicerContext,
    parent: str = "request",
) -> None:
    """Verify that any of the required arguments are supplied by the client.

    If arguments are missing, the context will be aborted

    Args:
        attrs: Names of the required parameters.
        obj: Current request message (e.g., a subclass of google.protobuf.message.Message).
        ctx: Current gRPC context.
        parent: Name of the parent message. Only used to compose more helpful error.
    """
    func = attrgetter(*attrs)
    attr_result = func(obj)

    if len(attrs) == 1:
        attr_result = [attr_result]

    if not any(attr_result):
        ctx.abort(
            grpc.StatusCode.INVALID_ARGUMENT,
            f"The message '{parent}' requires the following attributes: {attrs}.",
        )


def require_all(
    attrs: t.Collection[str],
    obj: object,
    ctx: grpc.ServicerContext,
    parent: str = "request",
) -> None:
    """Verify that all required arguments are supplied by the client.

    If arguments are missing, the context will be aborted

    Args:
        attrs: Names of the required parameters.
        obj: Current request message (e.g., a subclass of google.protobuf.message.Message).
        ctx: Current gRPC context.
        parent: Name of the parent message. Only used to compose more helpful error.
    """
    func = attrgetter(*attrs)
    attr_result = func(obj)

    if len(attrs) == 1:
        attr_result = [attr_result]

    if not all(attr_result):
        ctx.abort(
            grpc.StatusCode.INVALID_ARGUMENT,
            f"The message '{parent}' requires the following attributes: {attrs}.",
        )


def require_all_repeated(
    key: str,
    attrs: t.Collection[str],
    obj: object,
    ctx: grpc.ServicerContext,
) -> None:
    """Verify that all required arguments are supplied by the client.

    If arguments are missing, the context will be aborted

    Args:
        key: Name of repeated attribute.
        attrs: Names of the required parameters.
        obj: Current request message (e.g., a subclass of google.protobuf.message.Message).
        ctx: Current gRPC context.
    """
    func = attrgetter(key)

    for item in func(obj):
        require_all(attrs, item, ctx, key)


def require_any_repeated(
    key: str,
    attrs: t.Collection[str],
    obj: object,
    ctx: grpc.ServicerContext,
) -> None:
    """Verify that any required arguments are supplied by the client.

    If arguments are missing, the context will be aborted

    Args:
        key: Name of repeated attribute.
        attrs: Names of the required parameters.
        obj: Current request message (e.g., a subclass of google.protobuf.message.Message).
        ctx: Current gRPC context.
    """
    func = attrgetter(key)

    for item in func(obj):
        require_any(attrs, item, ctx, key)


def forbid_all(
    attrs: t.Collection[str],
    obj: object,
    ctx: grpc.ServicerContext,
    parent: str = "request",
) -> None:
    """Verify that no illegal combination of arguments is provided by the client.

    Args:
        attrs: Names of parameters which cannot occur at the same time.
        obj: Current request message (e.g., a subclass of google.protobuf.message.Message).
        ctx: Current gRPC context.
        parent: Name of the parent message. Only used to compose more helpful error.
    """
    func = attrgetter(*attrs)
    attr_result = func(obj)

    if len(attrs) == 1:
        attr_result = [attr_result]

    if all(attr_result):
        ctx.abort(
            grpc.StatusCode.INVALID_ARGUMENT,
            f"The message '{parent}' is not allowed to allowed to have the following parameter combination: {attrs}.",
        )


def full_service_name(pkg, service: str) -> str:
    return pkg.DESCRIPTOR.services_by_name[service].full_name


def _serve_single(
    bind_address: str,
    add_services: t.Callable[[grpc.Server], None],
    threads: int,
    reflection_services: t.Iterable[str] = tuple(),
    current_process: int = 1,
    total_processes: int = 1,
):
    """Helper function to start a server for a single process.

    Args:
        bind_address: Complete address consisting of hostname and port (e.g., `127.0.0.1:8000`)
        add_services: Function to inject the gRPC services into the server instance.
        current_process: Number of current process.
        total_processes: Total number of spawned processes.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=threads))
    add_services(server)

    if reflection_services:
        reflection.enable_server_reflection(
            [*reflection_services, reflection.SERVICE_NAME], server
        )

    server.add_insecure_port(bind_address)
    server.start()

    print(f"Worker {current_process}/{total_processes} serving on '{bind_address}'.")

    server.wait_for_termination()


def serve(
    host: str,
    port: int,
    add_services: t.Callable[[grpc.Server], None],
    threads: int = 1,
    processes: int = 1,
    reflection_services: t.Iterable[str] = tuple(),
):
    """Serve one or multiple gRPC services, optionally using multiprocessing.

    Args:
        host: Hostname of the server (e.g., `127.0.0.1`)
        ports: Start port for the server.
            Use `0` to let the server determine an open port.
        add_services: Function to inject the gRPC services into the server instance.
        threads: Number of workers in the gRPC thread pool.
        processes: Number of individual servers (each with their own port).

    Raises:
        ValueError: If `processes < 1` is given.
    """

    if processes < 1:
        raise ValueError("At least one process is required.")
    elif processes == 1:
        bind_addr = f"{host}:{port}"
        print(f"Connect to 'ipv4:{bind_addr}'.")

        _serve_single(bind_addr, add_services, threads, reflection_services)
    else:
        workers = []
        addresses = []

        for i, port in enumerate(range(port, port + processes)):
            bind_addr = f"{host}:{port}"
            addresses.append(bind_addr)

            worker = mp.Process(
                target=_serve_single,
                args=(
                    bind_addr,
                    add_services,
                    reflection_services,
                    i + 1,
                    processes,
                ),
            )
            worker.start()
            workers.append(worker)

        bind_addr = ",".join(addresses)
        print(f"Connect to 'ipv4:{bind_addr}'.")

        for worker in workers:
            worker.join()
