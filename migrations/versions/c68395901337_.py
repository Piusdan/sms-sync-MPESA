"""empty message

Revision ID: c68395901337
Revises: 367d08827e1f
Create Date: 2017-12-12 10:58:23.597247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c68395901337'
down_revision = '367d08827e1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('seen', sa.Boolean(), nullable=True))
    op.add_column('messages', sa.Column('seen_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'seen_on')
    op.drop_column('messages', 'seen')
    # ### end Alembic commands ###
