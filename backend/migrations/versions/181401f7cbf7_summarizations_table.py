"""summarizations table

Revision ID: 181401f7cbf7
Revises: 016c31b2cc81
Create Date: 2025-05-11 18:39:09.148088

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "181401f7cbf7"
down_revision: Union[str, None] = "016c31b2cc81"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "summarizations",
        sa.Column(
            "id", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("file_id", sa.UUID(), nullable=False),
        sa.Column("summary_text", sa.Text(), nullable=False),
        sa.Column("ai_model_used", sa.String(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["file_id"],
            ["uploaded_files.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("file_id"),
    )
    op.create_index(op.f("ix_summarizations_id"), "summarizations", ["id"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_summarizations_id"), table_name="summarizations")
    op.drop_table("summarizations")
    # ### end Alembic commands ###
