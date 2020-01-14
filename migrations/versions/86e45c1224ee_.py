"""empty message

Revision ID: 86e45c1224ee
Revises: 15db6e0e6daa
Create Date: 2020-01-14 11:46:37.413789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86e45c1224ee'
down_revision = '15db6e0e6daa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_object', sa.Column('blogType', sa.String(length=10), nullable=True))
    op.add_column('blog_object', sa.Column('image', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_object', 'image')
    op.drop_column('blog_object', 'blogType')
    # ### end Alembic commands ###
