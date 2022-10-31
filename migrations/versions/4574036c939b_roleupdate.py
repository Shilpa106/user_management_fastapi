"""roleupdate

Revision ID: 4574036c939b
Revises: 379395a58b52
Create Date: 2021-04-29 16:29:18.262546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4574036c939b'
down_revision = '379395a58b52'
branch_labels = None
depends_on = None


def upgrade():
    # op.add_column('groups', sa.Column('namev',sa.String(),nullable=True))
    op.alter_column('groups', sa.Column('namev', sa.String(), nullable=True))




def downgrade():
    op.drop_column('groups', sa.Column('names',sa.String(),nullable=True))


