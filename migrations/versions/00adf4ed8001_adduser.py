"""adduser

Revision ID: 00adf4ed8001
Revises: fddc06a60589
Create Date: 2021-05-03 10:27:36.382271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00adf4ed8001'
down_revision = 'fddc06a60589'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('User', sa.Column('date_of_birth',sa.String(),nullable=True))
    op.add_column('User', sa.Column('start_date',sa.String(),nullable=True))
    op.add_column('User', sa.Column('town',sa.String(),nullable=True))
    op.add_column('User', sa.Column('postcode',sa.String(),nullable=True))


def downgrade():
    pass
