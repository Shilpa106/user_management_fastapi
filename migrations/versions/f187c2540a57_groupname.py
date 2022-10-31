"""groupname

Revision ID: f187c2540a57
Revises: 07734a00b865
Create Date: 2021-04-30 10:42:51.874541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f187c2540a57'
down_revision = '07734a00b865'
branch_labels = None
depends_on = None


def upgrade():
    # op.alter_column('groups', 'namet', new_column_name='name', existing_type=sa.String())
    pass


def downgrade():
    pass
