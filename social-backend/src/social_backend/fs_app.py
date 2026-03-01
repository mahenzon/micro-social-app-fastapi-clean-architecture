import dishka_faststream
from dishka import make_async_container
from faststream import FastStream

from social_backend.config import settings
from social_backend.ioc import AppProvider
from social_backend.infra.broker import new_broker

container = make_async_container(AppProvider())


broker = new_broker(settings.broker.rabbit)
faststream_app = FastStream(broker)
dishka_faststream.setup_dishka(
    container,
    faststream_app,
    auto_inject=True,
)
