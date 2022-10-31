"""groupuseradd

Revision ID: 80cead81951d
Revises: 3f74964807a4
Create Date: 2021-05-09 11:11:37.784568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80cead81951d'
down_revision = '3f74964807a4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('groups', sa.Column('user_id', sa.String(), nullable=True))
    pass


def downgrade():
    pass
