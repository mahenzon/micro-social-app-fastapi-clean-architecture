from typing import TypeAlias
from uuid import UUID
from dataclasses import dataclass

UserID: TypeAlias = UUID


@dataclass(frozen=True, slots=True)
class User:

    id: UserID
    username: str
