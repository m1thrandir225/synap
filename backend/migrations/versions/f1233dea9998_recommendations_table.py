"""recommendations table

Revision ID: f1233dea9998
Revises: 9b784bc1bdb5
Create Date: 2025-04-16 20:51:17.623781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1233dea9998'
down_revision: Union[str, None] = '9b784bc1bdb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recommendations',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('file_id', sa.UUID(), nullable=False),
    sa.Column('learning_material_id', sa.UUID(), nullable=False),
    sa.Column('relevance_score', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['file_id'], ['uploaded_files.id'], ),
    sa.ForeignKeyConstraint(['learning_material_id'], ['learning_materials.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_recommendations_id'), 'recommendations', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_recommendations_id'), table_name='recommendations')
    op.drop_table('recommendations')
    # ### end Alembic commands ###
