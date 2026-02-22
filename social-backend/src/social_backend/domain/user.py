from typing import TypeAlias
from uuid import UUID
from pydantic import BaseModel, ConfigDict

UserID: TypeAlias = UUID


class UserBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    username: str


class UserCreate(UserBase):
    """
    Я понимаю, что это не тянет на доменную модель.
    Но мне же надо как-то прокидывать свойства при создании доменной модели.
    А при этом id предоставляет БД. Айди вообще не касается домена никак,
    мб модель юзера ниже нужно без id делать?
    """


class User(UserBase):

    id: UserID
