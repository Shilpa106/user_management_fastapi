"""groupupdate

Revision ID: 6eb4823d3ea8
Revises: 4574036c939b
Create Date: 2021-04-30 10:11:03.388895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6eb4823d3ea8'
down_revision = '4574036c939b'
branch_labels = None
depends_on = None


def upgrade():
    pass
    # op.add_column('groups', sa.Column('namev',sa.String(),nullable=True))
    # op.alter_column('groups', sa.Column('namev', sa.String(), nullable=True))
    # op.alter_column('groups', 'name',new_column_name='namev',existing_type=sa.String())



def downgrade():
    pass
    # op.drop_column('groups', sa.Column('names',sa.String(),nullable=True))