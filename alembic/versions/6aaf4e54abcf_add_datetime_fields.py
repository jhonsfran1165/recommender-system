"""add datetime fields

Revision ID: 6aaf4e54abcf
Revises: 98e20904518b
Create Date: 2021-07-20 14:56:36.951861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aaf4e54abcf'
down_revision = '98e20904518b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('copy',
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now())
    )

    op.add_column('copy',
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )


def downgrade():
    op.drop_column('created_at', 'author_name')
    op.drop_column('updated_at', 'author_name')
