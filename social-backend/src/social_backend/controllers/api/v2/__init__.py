from fastapi import APIRouter

from .users import router as users_router

router = APIRouter(
    prefix="/v2",
    tags=["v2"],
)
router.include_router(users_router)
