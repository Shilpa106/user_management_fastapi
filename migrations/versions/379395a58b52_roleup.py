"""roleup

Revision ID: 379395a58b52
Revises: ac271cb2d065
Create Date: 2021-04-29 16:10:40.315221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '379395a58b52'
down_revision = 'ac271cb2d065'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('groups', sa.Column('namev',sa.String(),nullable=True))



def downgrade():
    op.drop_column('groups', sa.Column('names',sa.String(),nullable=True))

