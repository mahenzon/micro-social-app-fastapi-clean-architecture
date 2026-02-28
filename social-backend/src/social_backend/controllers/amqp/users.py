from dishka import FromDishka
from faststream.rabbit import RabbitRouter

from social_backend.application.dto import NewUser
from social_backend.application.interactors import CreateUserInteractor
from social_backend.controllers.schemas import UserCreate

router = RabbitRouter()


@router.subscriber("create_user")
@router.publisher("created_users_ids")
async def handle(
    user_create: UserCreate,
    interactor: FromDishka[CreateUserInteractor],
) -> str:
    new_user = NewUser(
        username=user_create.username,
    )
    user = await interactor(new_user)
    return str(user.id)
