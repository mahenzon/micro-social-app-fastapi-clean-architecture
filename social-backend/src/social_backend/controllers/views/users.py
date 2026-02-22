from typing import Annotated
from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Path, HTTPException, Depends
from starlette import status

from social_backend.application.dto import NewUser
from social_backend.application.interactors import (
    GetUserInteractor,
    CreateUserInteractor,
)
from social_backend.controllers.schemas import UserRead, UserCreate
from social_backend.domain import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    route_class=DishkaRoute,
)


@router.get(
    "/{user_id}/",
    response_model=UserRead,
)
async def get_user_by_id(
    user_id: Annotated[
        UUID,
        Path(description="Book ID", title="Book ID"),
    ],
    get_user: FromDishka[GetUserInteractor],
) -> User:
    user = await get_user(user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {user_id} not found.",
    )


def new_user_dep(
    user_create: UserCreate,
) -> NewUser:
    return NewUser(
        username=user_create.username,
    )


@router.post(
    "/",
    response_model=UserRead,
)
async def create_user_view(
    new_user: Annotated[NewUser, Depends(new_user_dep)],
    create_user: FromDishka[CreateUserInteractor],
) -> User:
    return await create_user(new_user)
