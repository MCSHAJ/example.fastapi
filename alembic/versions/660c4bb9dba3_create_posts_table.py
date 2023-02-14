"""create posts table

Revision ID: 660c4bb9dba3
Revises: 
Create Date: 2023-02-10 08:56:33.873491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '660c4bb9dba3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('post')
    pass
