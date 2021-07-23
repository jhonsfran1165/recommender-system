"""add transaction type

Revision ID: ee91e2752bfc
Revises: 81d9f612b7a3
Create Date: 2021-07-23 11:03:49.320954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee91e2752bfc'
down_revision = '81d9f612b7a3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "transaction_type",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("trans_type_code", sa.String(), nullable=False),
        sa.Column("trans_type_description", sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now())
    )

    op.create_index(op.f("ix_transaction_type_code"), "transaction_type", ["trans_type_code"], unique=True)
    op.create_index(op.f("ix_transaction_type_description"), "transaction_type", ["trans_type_description"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_transaction_type_description"), table_name="transaction_type")
    op.drop_index(op.f("ix_transaction_type_code"), table_name="transaction_type")
    op.drop_table("transaction_type")
