"""dbchange

Revision ID: fc91cbd4d2c3
Revises: 311a943d7e09
Create Date: 2021-05-05 23:07:00.629657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc91cbd4d2c3'
down_revision = '311a943d7e09'
branch_labels = None
depends_on = None


def upgrade():
    # op.drop_column('User', 'subgroup_id')
    pass


def downgrade():
    pass
