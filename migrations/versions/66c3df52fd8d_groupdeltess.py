"""groupdeltess

Revision ID: 66c3df52fd8d
Revises: b995a747d54a
Create Date: 2021-04-30 10:29:29.761297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66c3df52fd8d'
down_revision = 'b995a747d54a'
branch_labels = None
depends_on = None


def upgrade():
    # op.drop_constraint('groups', 'names')
    pass


def downgrade():
    pass

