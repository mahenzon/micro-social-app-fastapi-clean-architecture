from uuid import UUID
from dataclasses import dataclass

type UserID = UUID


@dataclass(frozen=True, slots=True)
class User:

    id: UserID
    username: str
