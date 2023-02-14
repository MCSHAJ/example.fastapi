"""add content to posts table

Revision ID: 5d9bcdd8c223
Revises: ccb9d56a2088
Create Date: 2023-02-14 07:03:40.983171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d9bcdd8c223'
down_revision = 'ccb9d56a2088'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
