"""Pushing changes

Revision ID: 5a9eb16d5753
Revises: 4d9613e97da3
Create Date: 2024-12-19 16:44:16.291660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy import Text


# revision identifiers, used by Alembic.
revision: str = '5a9eb16d5753'
down_revision: Union[str, None] = '4d9613e97da3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###