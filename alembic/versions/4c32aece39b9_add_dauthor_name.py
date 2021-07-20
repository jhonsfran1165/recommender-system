"""add dauthor name

Revision ID: 4c32aece39b9
Revises: 6aaf4e54abcf
Create Date: 2021-07-20 15:05:29.594313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c32aece39b9'
down_revision = '6aaf4e54abcf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('copy',
        sa.Column("author_name", sa.String(), nullable=True),
    )


def downgrade():
    op.drop_column('copy', 'author_name')
