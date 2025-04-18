"""summarization file unique constraint

Revision ID: f10c9714b945
Revises: 56c7b956ba42
Create Date: 2025-04-16 17:19:11.872627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f10c9714b945'
down_revision: Union[str, None] = '56c7b956ba42'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'summarizations', ['file_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'summarizations', type_='unique')
    # ### end Alembic commands ###
