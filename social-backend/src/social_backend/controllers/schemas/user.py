from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, StringConstraints


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    username: Annotated[
        str,
        StringConstraints(
            min_length=3,
            max_length=32,
        ),
    ]


class UserRead(UserBase):
    id: UUID
