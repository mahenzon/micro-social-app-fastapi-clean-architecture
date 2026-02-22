from pydantic import BaseModel, SecretStr
from sqlalchemy import URL


class SQLAlchemyConfig(BaseModel):
    pool_size: int = 20
    max_overflow: int = 5
    echo: bool = False


class PostgresConfig(BaseModel):
    name: str = "social_app"
    host: str = "localhost"
    port: int = 5432
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
