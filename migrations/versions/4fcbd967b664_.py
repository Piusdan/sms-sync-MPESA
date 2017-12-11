"""empty message

Revision ID: 4fcbd967b664
Revises: 77aa60b02400
Create Date: 2017-12-11 21:01:47.353879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fcbd967b664'
down_revision = '77aa60b02400'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('text', sa.String(length=255), nullable=True),
    sa.Column('from_', sa.String(), nullable=True),
    sa.Column('to_', sa.String(), nullable=True),
    sa.Column('sent_on', sa.DateTime(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_index(op.f('ix_messages_text'), 'messages', ['text'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_messages_text'), table_name='messages')
    op.drop_table('messages')
    # ### end Alembic commands ###
