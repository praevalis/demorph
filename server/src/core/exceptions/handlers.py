import traceback
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from src.core.logging import logger
from src.core.exceptions.exceptions import (
    BadRequest,
    Unauthorized,
    Forbidden,
    NotFound,
    UnprocessableEntity,
    InternalServerError,
)


def create_error_response(exc: Exception, status_code: int) -> JSONResponse:
    """
    Creates standard error response for given exception.

    Args:
        exc: Exception to create response.
        status_code: Status code for the error response.

    Returns:
        JSONResponse: Created response.
    """
    return JSONResponse(
        status_code=status_code,
        content={
            'error': exc.__class__.__name__,
            'message': str(exc),
            'status_code': status_code,
        },
    )


def log_exception(request: Request, exc: Exception) -> None:
    """
    Logs exception.

    Args:
        request: Request in which the error occurred.
        exc: Exception to be logged.

    Returns:
        None: Only logs the exception.
    """
    logger.error(
        f'\n--- Exception Occurred ---\n'
        f'URL: {request.url.path}\n'
        f'Method: {request.method}\n'
        f'Exception: {str(exc)}\n'
        f'Traceback:\n{traceback.format_exc()}'
    )


def register_error_handlers(app: FastAPI) -> None:
    """
    Registers all the error handlers to the FastAPI application.

    Args:
        app: Instantiated FastAPI application.

    Returns:
        None: Registers without returning.
    """

    @app.exception_handler(BadRequest)
    async def handle_bad_request(request: Request, exc: BadRequest) -> JSONResponse:
        log_exception(request, exc)
        return create_error_response(exc, exc.status_code)

    @app.exception_handler(Unauthorized)
    async def handle_unauthorized(request: Request, exc: Unauthorized) -> JSONResponse:
        log_exception(request, exc)
        return create_error_response(exc, exc.status_code)

    @app.exception_handler(Forbidden)
    async def handle_forbidden(request: Request, exc: Forbidden) -> JSONResponse:
        log_exception(request, exc)
        return create_error_response(exc, exc.status_code)

    @app.exception_handler(NotFound)
    async def handle_not_found(request: Request, exc: NotFound) -> JSONResponse:
        log_exception(request, exc)
        return create_error_response(exc, exc.status_code)

    @app.exception_handler(UnprocessableEntity)
    async def handle_unprocessable_entity(
        request: Request, exc: UnprocessableEntity
    ) -> JSONResponse:
        log_exception(request, exc)
        return create_error_response(exc, exc.status_code)

    @app.exception_handler(InternalServerError)
    async def handle_internal_server_error(request: Request, exc: InternalServerError):
        log_exception(request, exc)
        return create_error_response(exc, exc.status_code)

    # This is the catch-all handler, for unhandled exceptions
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        log_exception(request, exc)
        return JSONResponse(
            status_code=500,
            content={
                'error': 'Internal Server Error',
                'message': 'An unexpected error occurred.',
                'status_code': 500,
            },
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        log_exception(request, exc)
        return JSONResponse(
            status_code=422,
            content={
                'error': 'RequestValidationError',
                'message': exc.errors(),
                'body': exc.body if hasattr(exc, 'body') else None,
                'status_code': 422,
            },
        )
