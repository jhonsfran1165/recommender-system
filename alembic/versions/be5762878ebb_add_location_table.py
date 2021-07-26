"""add location table

Revision ID: be5762878ebb
Revises: ee91e2752bfc
Create Date: 2021-07-26 07:24:51.462619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be5762878ebb'
down_revision = 'ee91e2752bfc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "location",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("location_code", sa.String(), nullable=False),
        sa.Column("location_name", sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now())
    )

    op.create_index(op.f("ix_location_code"), "location", ["location_code"], unique=True)
    op.create_index(op.f("ix_location_name"), "location", ["location_name"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_location_name"), table_name="location")
    op.drop_index(op.f("ix_location_code"), table_name="location")
    op.drop_table("location")
