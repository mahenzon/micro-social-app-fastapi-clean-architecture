import logging
from typing import Literal

from fastapi import APIRouter, status

from social_backend.controllers.schemas import UserCreate
from social_backend.fs_app import broker

log = logging.getLogger(__name__)


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(
    "/",
    status_code=status.HTTP_202_ACCEPTED,
)
async def create_user(user: UserCreate) -> Literal["ok"]:
    frame = await broker.publish(
        message=user,
        queue="create_user",
        persist=True,
    )
    log.info("frame: %s", frame)
    return "ok"
