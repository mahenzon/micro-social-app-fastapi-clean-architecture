from pydantic import BaseModel


class RabbitConfig(BaseModel):
    host: str = "localhost"
    port: int = 5672
    virtualhost: str = "/"
    username: str = "guest"
    password: str = "guest"


class BrokerConfig(BaseModel):
    rabbit: RabbitConfig = RabbitConfig()
