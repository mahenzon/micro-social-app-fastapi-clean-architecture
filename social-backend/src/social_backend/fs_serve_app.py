__all__ = (
    "broker",
    "faststream_app",
)

from dishka import make_async_container
from social_backend.ioc import AppProvider
from social_backend.controllers.amqp.users import router as users_router
from social_backend.fs_app import broker, faststream_app

container = make_async_container(AppProvider())

broker.include_router(users_router)
