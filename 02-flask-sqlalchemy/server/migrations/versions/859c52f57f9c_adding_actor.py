"""adding actor

Revision ID: 859c52f57f9c
Revises: 40a8c9dbed1e
Create Date: 2023-10-03 14:28:29.382609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '859c52f57f9c'
down_revision = '40a8c9dbed1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('actors')
    # ### end Alembic commands ###
