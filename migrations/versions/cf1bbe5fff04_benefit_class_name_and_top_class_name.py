"""Benefit class name and top class name

Revision ID: cf1bbe5fff04
Revises: 2e4cdbf1d606
Create Date: 2024-09-05 17:50:28.360615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf1bbe5fff04'
down_revision = '2e4cdbf1d606'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('benefit', schema=None) as batch_op:
        batch_op.add_column(sa.Column('class_name', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('top_class_name', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('benefit', schema=None) as batch_op:
        batch_op.drop_column('top_class_name')
        batch_op.drop_column('class_name')

    # ### end Alembic commands ###
