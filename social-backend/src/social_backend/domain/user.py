from dataclasses import dataclass
from typing import TypeAlias
from uuid import UUID

UserID: TypeAlias = UUID


@dataclass(slots=True)
class User:
    id: UserID
    username: str
