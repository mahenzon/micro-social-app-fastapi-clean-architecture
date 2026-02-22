import uuid

from sqlalchemy import func, UUID, CheckConstraint, and_
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import CITEXT

from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.uuidv7(),
    )
    username: Mapped[str] = mapped_column(
        CITEXT,
        unique=True,
    )

    __table_args__ = (
        # username length
        CheckConstraint(
            and_(
                func.length(username) >= 3,
                func.length(username) <= 32,
            ),
            name="name_length",
        ),
    )
