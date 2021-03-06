"""empty message

Revision ID: 60548d0505ea
Revises: cb8e1f876bc3
Create Date: 2016-11-15 19:10:12.922256

"""

# revision identifiers, used by Alembic.
revision = '60548d0505ea'
down_revision = 'cb8e1f876bc3'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('email_from', sa.String(), nullable=True))
    op.add_column('settings', sa.Column('email_from_name', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'email_from_name')
    op.drop_column('settings', 'email_from')
    ### end Alembic commands ###
