"""rename fio -> fullname for User model

Revision ID: 99d1829f7bb4
Revises: a6b2d4b904d3
Create Date: 2025-02-28 15:01:35.962274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99d1829f7bb4'
down_revision: Union[str, None] = 'a6b2d4b904d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        table_name='users', column_name='fio',
        nullable=False, new_column_name='fullname'
    )


def downgrade() -> None:
    op.alter_column(
        table_name='users', column_name='fullname',
        new_column_name='fio'
    )
