from typing import TypeAlias
from uuid import UUID
from pydantic import BaseModel

UserID: TypeAlias = UUID


class User(BaseModel):
    id: UserID
    username: str
