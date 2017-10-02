"""initial migration

Revision ID: 416bc965a99e
Revises: 1b966e7f4b9e
Create Date: 2017-10-02 18:27:07.341819

"""

# revision identifiers, used by Alembic.
revision = '416bc965a99e'
down_revision = '1b966e7f4b9e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
