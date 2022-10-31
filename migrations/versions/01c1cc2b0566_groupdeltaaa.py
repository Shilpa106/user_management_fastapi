"""groupdeltaaa

Revision ID: 01c1cc2b0566
Revises: 66c3df52fd8d
Create Date: 2021-04-30 10:31:45.113419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01c1cc2b0566'
down_revision = '66c3df52fd8d'
branch_labels = None
depends_on = None


def upgrade():
    # op.drop_column('groups','names')
    pass


def downgrade():
    pass
