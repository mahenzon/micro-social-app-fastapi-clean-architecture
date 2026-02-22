from typing import Any

from pydantic import BaseModel, SecretStr
from sqlalchemy import URL


class SQLAlchemyConfig(BaseModel):
    pool_size: int = 20
    max_overflow: int = 5
    echo: bool = False
    connect_timeout: int = 5

    @property
    def connect_args(self) -> dict[str, Any]:
        return {
            "connect_timeout": self.connect_timeout,
        }


class PostgresConfig(BaseModel):
    name: str = "social_app"
    host: str = "localhost"
    port: int = 5432
    schema_name: str = "social_backend"
    user: str = "app"
    password: SecretStr


class DatabaseConfig(BaseModel):
    pg: PostgresConfig
    sqla: SQLAlchemyConfig = SQLAlchemyConfig()

    @property
    def async_url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            database=self.pg.name,
            host=self.pg.host,
            port=self.pg.port,
            username=self.pg.user,
            password=self.pg.password.get_secret_value(),
        )
