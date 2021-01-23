"""empty message

Revision ID: 0a513cffd548
Revises: 7f72dcf319b7
Create Date: 2021-01-23 21:16:27.980730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a513cffd548'
down_revision = '7f72dcf319b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_fair', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trade_group',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('was_benefitted', sa.Boolean(), nullable=True),
    sa.Column('trade_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trade_id'], ['trade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trade_pokemon',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('trade_group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trade_group_id'], ['trade_group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trade_pokemon')
    op.drop_table('trade_group')
    op.drop_table('trade')
    # ### end Alembic commands ###
