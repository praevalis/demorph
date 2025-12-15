from fastapi import FastAPI
from typing import Optional, Callable
from contextlib import AbstractAsyncContextManager

from src.core.lifespan import lifespan
from src.core.middlewares import cors_middleware
from src.user.routers import router as user_router
from src.auth.routers import router as auth_router
from src.user.dependencies import get_user_service
from src.auth.dependencies import get_user_provider
from src.core.exceptions.handlers import register_error_handlers
from src.core.metadata import title, version, description, tags


def create_app(init_db: bool = True) -> FastAPI:
    """
    Factory function for FastAPI app.

    Args:
        init_db: Indicates whether to initialize the database. Must be False for testing.

    Returns:
        FastAPI: Initialized app.
    """
    app_lifespan: Optional[Callable[[FastAPI], AbstractAsyncContextManager[None]]] = (
        None
    )

    if init_db:
        app_lifespan = lifespan

    app = FastAPI(
        title=title,
        version=version,
        description=description,
        openapi_tags=tags,
        lifespan=app_lifespan,
    )

    register_error_handlers(app)

    cors_middleware.add(app)

    app.dependency_overrides[get_user_provider] = get_user_service

    app.include_router(auth_router)
    app.include_router(user_router)

    return app


api = create_app()
