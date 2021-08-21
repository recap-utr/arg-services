import contextlib
import socket
import traceback
import typing as t
from concurrent import futures
from operator import attrgetter

import grpc
import grpc.aio
from grpc_reflection.v1alpha import reflection


async def handle_except(ex: Exception, ctx: grpc.aio.ServicerContext) -> None:
    """Handler that can be called when handling an exception.

    It will pass the traceback to the gRPC client and abort the context.

    Args:
        ex: Exception that occured.
        ctx: Current gRPC context.
    """

    msg = "".join(traceback.TracebackException.from_exception(ex).format())
    await ctx.abort(grpc.StatusCode.UNKNOWN, msg)


async def require_any(
    attrs: t.Collection[str],
    obj: object,
    ctx: grpc.aio.ServicerContext,
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
        await ctx.abort(
            grpc.StatusCode.INVALID_ARGUMENT,
            f"The message '{parent}' requires the following attributes: {attrs}.",
        )


async def require_all(
    attrs: t.Collection[str],
    obj: object,
    ctx: grpc.aio.ServicerContext,
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
        await ctx.abort(
            grpc.StatusCode.INVALID_ARGUMENT,
            f"The message '{parent}' requires the following attributes: {attrs}.",
        )


async def require_all_repeated(
    key: str,
    attrs: t.Collection[str],
    obj: object,
    ctx: grpc.aio.ServicerContext,
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
        await require_all(attrs, item, ctx, key)


async def require_any_repeated(
    key: str,
    attrs: t.Collection[str],
    obj: object,
    ctx: grpc.aio.ServicerContext,
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
        await require_any(attrs, item, ctx, key)


async def forbid_all(
    attrs: t.Collection[str],
    obj: object,
    ctx: grpc.aio.ServicerContext,
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
        await ctx.abort(
            grpc.StatusCode.INVALID_ARGUMENT,
            f"The message '{parent}' is not allowed to allowed to have the following parameter combination: {attrs}.",
        )


def full_service_name(pkg, service: str) -> str:
    return pkg.DESCRIPTOR.services_by_name[service].full_name


try:
    import aiomultiprocess as mp

    async def _serve_single(
        bind_address: str,
        add_services: t.Callable[[grpc.aio.Server], None],
        reflection_services: t.Iterable[str] = tuple(),
        reuse_port: bool = False,
        current_process: int = 1,
        total_processes: int = 1,
    ):
        """Helper function to start a server for a single process.

        Args:
            bind_address: Complete address consisting of hostname and port (e.g., `127.0.0.1:8000`)
            add_services: Function to inject the gRPC services into the server instance.
            reuse_port: If using multiple processes, the port has to be reused.
            current_process: Number of current process.
            total_processes: Total number of spawned processes.
        """
        server = grpc.aio.server(
            options=(("grpc.aio.so_reuseport", 1 if reuse_port else 0),),
        )
        add_services(server)

        if reflection_services:
            reflection.enable_server_reflection(
                [*reflection_services, reflection.SERVICE_NAME], server
            )

        server.add_insecure_port(bind_address)
        await server.start()

        print(
            f"Worker {current_process}/{total_processes} serving on '{bind_address}'."
        )

        await server.wait_for_termination()

    async def serve(
        host: str,
        port: int,
        add_services: t.Callable[[grpc.aio.Server], None],
        processes: int,
        reuse_port: bool = False,
        reflection_services: t.Iterable[str] = tuple(),
    ):
        """Serve one or multiple gRPC services, optionally using multiprocessing.

        Args:
            host: Hostname of the server (e.g., `127.0.0.1`)
            ports: Start port for the server.
                Use `0` to let the server determine an open port.
            add_services: Function to inject the gRPC services into the server instance.
            processes: Number of workers.
            reuse_port: On Linux systems, the OS can automatically perform load balancing.
                If true, the option `SO_REUSEPORT` will be set.

        Raises:
            ValueError: If `processes < 0` is given.
        """

        reuse_port = reuse_port and (processes == 1)

        if processes == 1:
            with _reserve_port(port) as actual_port:
                bind_addr = f"{host}:{actual_port}"
                print(f"Connect to 'ipv4:{bind_addr}'.")

                await _serve_single(bind_addr, add_services, reflection_services)
        else:
            socks = []
            workers = []
            addresses = set()

            for i, port in enumerate(range(port, port + processes)):
                sock = _open_port(port)
                socks.append(socks)
                actual_port = _port_number(sock)
                bind_addr = f"{host}:{actual_port}"
                addresses.add(bind_addr)

                worker = mp.Process(
                    target=_serve_single,
                    args=(
                        bind_addr,
                        add_services,
                        reflection_services,
                        reuse_port,
                        i + 1,
                        processes,
                    ),
                )
                worker.start()
                workers.append(worker)

            bind_addr = ",".join(addresses)
            print(f"Connect to 'ipv4:{bind_addr}'.")

            for worker in workers:
                await worker.join()

            for sock in socks:
                _close_port(sock)

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

        sock = _open_port(port, reuse_port)

        try:
            yield _port_number(sock)
        finally:
            _close_port(sock)

    def _close_port(sock: socket.socket) -> None:
        sock.close()

    def _port_number(sock: socket.socket) -> int:
        return sock.getsockname()[1]

    def _open_port(port: int = 0, reuse_port: bool = False) -> socket.socket:
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

        if reuse_port:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

            if sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT) == 0:
                raise RuntimeError("Failed to set SO_REUSEPORT.")

        sock.bind(("", port))

        return sock


except ImportError:
    pass
