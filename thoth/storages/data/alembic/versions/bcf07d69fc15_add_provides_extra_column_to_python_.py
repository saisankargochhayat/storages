"""Add provides extra column to Python metadata

Revision ID: bcf07d69fc15
Revises: ff18da87f7c1
Create Date: 2019-10-22 11:21:47.015295+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcf07d69fc15'
down_revision = 'ff18da87f7c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('python_package_metadata', sa.Column('provides_extra', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('python_package_metadata', 'provides_extra')
    # ### end Alembic commands ###
