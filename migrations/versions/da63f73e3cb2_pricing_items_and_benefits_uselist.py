"""Pricing items and benefits uselist

Revision ID: da63f73e3cb2
Revises: cf1bbe5fff04
Create Date: 2024-09-11 09:10:59.252385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da63f73e3cb2'
down_revision = 'cf1bbe5fff04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('page_benefits',
    sa.Column('page_id', sa.Integer(), nullable=False),
    sa.Column('benefits_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['benefits_id'], ['benefits.id'], ),
    sa.ForeignKeyConstraint(['page_id'], ['page.id'], ),
    sa.PrimaryKeyConstraint('page_id', 'benefits_id')
    )
    op.create_table('page_pricing',
    sa.Column('page_id', sa.Integer(), nullable=False),
    sa.Column('pricing_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['page_id'], ['page.id'], ),
    sa.ForeignKeyConstraint(['pricing_id'], ['pricing.id'], ),
    sa.PrimaryKeyConstraint('page_id', 'pricing_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('page_pricing')
    op.drop_table('page_benefits')
    # ### end Alembic commands ###
