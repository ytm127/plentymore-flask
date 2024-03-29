"""adding about me attribute 

Revision ID: 1d97e12f0fc7
Revises: 6984d2835f2f
Create Date: 2019-06-02 14:30:06.934743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d97e12f0fc7'
down_revision = '6984d2835f2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
