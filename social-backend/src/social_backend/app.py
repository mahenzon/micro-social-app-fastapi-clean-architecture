from fastapi import FastAPI
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

from social_backend.config import settings
from social_backend.controllers.views import router
from social_backend.ioc import AppProvider

container = make_async_container(AppProvider())


def get_fastapi_app() -> FastAPI:
    fastapi_app = FastAPI(
        title=settings.app.title,
    )

    fastapi_app.include_router(router)

    setup_dishka(container, fastapi_app)

    return fastapi_app


def get_app() -> FastAPI:
    fastapi_app = get_fastapi_app()

    return fastapi_app


app = get_app()
