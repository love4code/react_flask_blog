"""empty message

Revision ID: 61fcdd132870
Revises: e571ec1a31d9
Create Date: 2016-09-08 22:50:49.070852

"""

# revision identifiers, used by Alembic.
revision = '61fcdd132870'
down_revision = 'e571ec1a31d9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], [u'articles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [u'users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    ### end Alembic commands ###
