"""create table users

Revision ID: 3d6f629f564d
Revises: 395eddb0178f
Create Date: 2026-02-22 21:37:11.509321

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "3d6f629f564d"
down_revision: Union[str, Sequence[str], None] = "395eddb0178f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("uuidv7()"),
            nullable=False,
        ),
        sa.Column(
            "username",
            postgresql.CITEXT(),
            nullable=False,
        ),
        sa.CheckConstraint(
            "length(username) >= 3 AND length(username) <= 32",
            name=op.f("ck_users_username_length"),
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_users"),
        ),
        sa.UniqueConstraint(
            "username",
            name=op.f("uq_users_username"),
        ),
        schema="social_backend",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table(
        "users",
        schema="social_backend",
    )
