"""Main module for the files API."""

import pydantic
from fastapi import FastAPI
from fastapi.routing import APIRoute
from mangum import Mangum

from deepcuts_api.errors import (
    handle_broad_exceptions,
    handle_pydantic_validation_errors,
)
from deepcuts_api.routes import ROUTER
from deepcuts_api.settings import Settings


def custom_generate_unique_id(route: APIRoute):
    """Generate a unique ID for a FastAPI route."""
    return f"{route.tags[0]}-{route.name}"


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create a FastAPI application with the specified S3 bucket name."""
    settings = settings or Settings()

    version = settings.version

    app = FastAPI(
        title="Deepcuts API",
        description="An API to access music artist metadata and recommendations.",
        generate_unique_id_function=custom_generate_unique_id,
        version=version,
    )
    app.state.settings = settings

    app.include_router(ROUTER)
    app.add_exception_handler(
        exc_class_or_status_code=pydantic.ValidationError,
        handler=handle_pydantic_validation_errors,  # type: ignore
    )
    app.middleware("http")(handle_broad_exceptions)

    return app


if __name__ == "__main__":
    import uvicorn  # type: ignore

    app: FastAPI = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)

    app = create_app()
    handler = Mangum(app)
