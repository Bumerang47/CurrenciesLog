"""empty message

Revision ID: 84c0736db973
Revises: 55afa9fa946d
Create Date: 2019-05-22 05:27:13.184446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84c0736db973'
down_revision = '55afa9fa946d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rate', sa.Column('currency_id', sa.Integer(), nullable=False))
    op.create_unique_constraint('_ticker__date', 'rate', ['currency_id', 'date'])
    op.create_foreign_key(None, 'rate', 'currency', ['currency_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rate', type_='foreignkey')
    op.drop_constraint('_ticker__date', 'rate', type_='unique')
    op.drop_column('rate', 'currency_id')
    # ### end Alembic commands ###
