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
    address: str,
    add_services: t.Callable[[grpc.Server], None],
    threads: int,
    reflection_services: t.Iterable[str] = tuple(),
    worker_id: int = 1,
):
    """Helper function to start a server for a single process.

    Args:
        address: Complete address consisting of hostname and port (e.g., `127.0.0.1:8000`)
        add_services: Function to inject the gRPC services into the server instance.
        threads: Number of workers for the ThreadPoolExecutor.
        reflection_services: Name of all services this server offers.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=threads))
    add_services(server)

    if reflection_services:
        reflection.enable_server_reflection(
            [*reflection_services, reflection.SERVICE_NAME], server
        )

    server.add_insecure_port(address)
    server.start()

    print(f"Worker {worker_id} serving on '{address}'.")

    server.wait_for_termination()


def serve(
    address: str,
    add_services: t.Callable[[grpc.Server], None],
    reflection_services: t.Iterable[str],
    threads: int = 1,
):
    """Serve one or multiple gRPC services, optionally using multiprocessing.

    Args:
        address: Connection string the server should listen on.
            Should be given in the form `host:port`, example: `127.0.0.1:6789`.
            If multiple processes should be started, use the notation `host:port1,host:port2,...`
        add_services: Function to inject the gRPC services into the server instance.
        reflection_services: List of services this server supports.
            Use the provided function `arg_services_helper.full_service_name` to get the correct names.
        threads: Number of workers in the gRPC thread pool.

    Raises:
        ValueError: If `processes < 1` is given.
    """

    urls = [url.strip() for url in address.split(",")]

    if len(urls) == 1:
        _serve_single(urls[0], add_services, threads, reflection_services)
    else:
        workers = []

        for url in urls:
            worker = mp.Process(
                target=_serve_single,
                args=(
                    url,
                    add_services,
                    reflection_services,
                ),
            )
            worker.start()
            workers.append(worker)

        print("All workers have started, please connect to your provided address.")

        for worker in workers:
            worker.join()
