from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

from social_backend.config import settings
from social_backend.controllers.api import router as api_router
from social_backend.ioc import AppProvider
from social_backend.fs_app import broker

container = make_async_container(AppProvider())


@asynccontextmanager
async def lifespan(
    _: FastAPI,
) -> AsyncGenerator[None]:
    await broker.start()
    yield
    await broker.stop()


def get_fastapi_app() -> FastAPI:
    fastapi_app = FastAPI(
        title=settings.app.title,
        lifespan=lifespan,
    )

    fastapi_app.include_router(api_router)

    setup_dishka(container, fastapi_app)

    return fastapi_app


def get_app() -> FastAPI:
    fastapi_app = get_fastapi_app()

    return fastapi_app


app = get_app()
