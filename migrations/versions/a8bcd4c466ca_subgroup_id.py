"""subgroup id

Revision ID: a8bcd4c466ca
Revises: 56bc8b4be8a7
Create Date: 2021-05-02 14:44:42.127444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8bcd4c466ca'
down_revision = '56bc8b4be8a7'
branch_labels = None
depends_on = None


def upgrade():
    pass
    # op.drop_column('User', 'subgroup_id')


def downgrade():
    pass
