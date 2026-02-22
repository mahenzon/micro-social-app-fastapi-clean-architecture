from typing import TypeAlias
from uuid import UUID
from pydantic import BaseModel, ConfigDict

UserID: TypeAlias = UUID


class User(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UserID
    username: str
