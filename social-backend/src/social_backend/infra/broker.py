from faststream.rabbit import RabbitBroker
from faststream.security import SASLPlaintext
from social_backend.config.broker import RabbitConfig


def new_broker(config: RabbitConfig) -> RabbitBroker:
    return RabbitBroker(
        host=config.host,
        port=config.port,
        virtualhost=config.virtualhost,
        security=SASLPlaintext(
            username=config.username,
            password=config.password,
        ),
    )
