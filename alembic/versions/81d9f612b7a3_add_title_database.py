"""add title database

Revision ID: 81d9f612b7a3
Revises: 4c32aece39b9
Create Date: 2021-07-22 08:27:10.816105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81d9f612b7a3'
down_revision = '4c32aece39b9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "title",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title_name", sa.String(), nullable=False),
        sa.Column("subtitle", sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now())
    )

    op.create_index(op.f("ix_title_name"), "title", ["title_name"], unique=False)
    op.create_index(op.f("ix_title_id"), "title", ["id"], unique=False)
    op.create_index(op.f("ix_title_subtitle"), "title", ["subtitle"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_title_name"), table_name="title")
    op.drop_index(op.f("ix_title_id"), table_name="title")
    op.drop_index(op.f("ix_title_subtitle"), table_name="title")
    op.drop_table("title")
