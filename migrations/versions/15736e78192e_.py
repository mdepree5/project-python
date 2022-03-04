"""empty message

Revision ID: 15736e78192e
Revises: 
Create Date: 2022-03-04 16:54:34.750607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15736e78192e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('cheatsheets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('dependencies', sa.Text(), nullable=False),
    sa.Column('media_url', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('writer_id', sa.Integer(), nullable=False),
    sa.Column('cheatsheet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cheatsheet_id'], ['cheatsheets.id'], ),
    sa.ForeignKeyConstraint(['writer_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('steps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('media_url', sa.String(length=255), nullable=False),
    sa.Column('cheatsheet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cheatsheet_id'], ['cheatsheets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('steps')
    op.drop_table('comments')
    op.drop_table('cheatsheets')
    op.drop_table('users')
    # ### end Alembic commands ###
