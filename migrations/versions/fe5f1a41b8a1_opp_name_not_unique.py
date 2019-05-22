"""opp name not unique

Revision ID: fe5f1a41b8a1
Revises: 0752213a4726
Create Date: 2019-05-21 21:07:06.371121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe5f1a41b8a1'
down_revision = '0752213a4726'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_opportunity_name', table_name='opportunity')
    op.create_index(op.f('ix_opportunity_name'), 'opportunity', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_opportunity_name'), table_name='opportunity')
    op.create_index('ix_opportunity_name', 'opportunity', ['name'], unique=True)
    # ### end Alembic commands ###
