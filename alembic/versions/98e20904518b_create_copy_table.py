"""create copy table

Revision ID: 98e20904518b
Revises: 051f512804af
Create Date: 2021-07-20 12:50:48.291956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98e20904518b'
down_revision = '051f512804af'
branch_labels = None
depends_on = None


def upgrade():
    # COPIES
    op.create_table(
        "copy",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("copy_title", sa.String(), nullable=False),
        sa.Column("title_id", sa.String(), nullable=True),
        sa.Column("medium_type", sa.String(), nullable=True),
        sa.Column("pr_classmark", sa.String(), nullable=True),
        sa.Column("shelfmark", sa.String(), nullable=True),
        sa.Column("bar_code", sa.String(), nullable=True),
        sa.Column("location", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_copy_title"), "copy", ["copy_title"], unique=False)
    op.create_index(op.f("ix_copy_id"), "copy", ["id"], unique=False)
    op.create_index(op.f("ix_copy_title_id"), "copy", ["title_id"], unique=False)


def downgrade():
    # COPIES
    op.drop_index(op.f("ix_copy_title_id"), table_name="copy")
    op.drop_index(op.f("ix_copy_id"), table_name="copy")
    op.drop_index(op.f("ix_copy_title"), table_name="copy")
    op.drop_table("copy")
