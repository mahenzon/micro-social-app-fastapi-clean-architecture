from pydantic import BaseModel


class AppConfig(BaseModel):
    title: str = "Social App Backend"
    host: str = "0.0.0.0"
    port: int = 8000
