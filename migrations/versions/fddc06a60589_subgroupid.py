"""subgroupid

Revision ID: fddc06a60589
Revises: a8bcd4c466ca
Create Date: 2021-05-02 14:50:59.540556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fddc06a60589'
down_revision = 'a8bcd4c466ca'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('User', 'subgroup_id')


def downgrade():
    pass
