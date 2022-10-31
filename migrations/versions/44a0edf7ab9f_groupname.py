"""groupname

Revision ID: 44a0edf7ab9f
Revises: 6eb4823d3ea8
Create Date: 2021-04-30 10:18:31.756416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44a0edf7ab9f'
down_revision = '6eb4823d3ea8'
branch_labels = None
depends_on = None

def upgrade():
    pass
    # op.add_column('groups', sa.Column('namev',sa.String(),nullable=True))
    # op.alter_column('groups', sa.Column('namev', sa.String(), nullable=True))
    # op.alter_column('groups', 'name',new_column_name='namet',existing_type=sa.String())



def downgrade():
    pass
    # op.drop_column('groups','names')