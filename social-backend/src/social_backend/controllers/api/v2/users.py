from typing import Literal

from fastapi import APIRouter, status

from social_backend.controllers.schemas import UserCreate

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(
    "/",
    status_code=status.HTTP_202_ACCEPTED,
)
async def create_user(user: UserCreate) -> Literal["ok"]:
    return "ok"
