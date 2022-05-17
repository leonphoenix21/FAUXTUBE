"""empty message

Revision ID: f69add6e9c02
Revises: 85a469f32ea0
Create Date: 2022-05-16 22:23:22.821642

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f69add6e9c02'
down_revision = '85a469f32ea0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('avatar', sa.String(length=255), nullable=False))
    op.add_column('comments', sa.Column('firstname', sa.String(length=40), nullable=False))
    op.add_column('comments', sa.Column('lastname', sa.String(length=40), nullable=False))
    op.drop_column('comments', 'song_timestamp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('song_timestamp', postgresql.TIME(), autoincrement=False, nullable=True))
    op.drop_column('comments', 'lastname')
    op.drop_column('comments', 'firstname')
    op.drop_column('comments', 'avatar')
    # ### end Alembic commands ###