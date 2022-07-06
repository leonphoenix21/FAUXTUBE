"""empty message

Revision ID: 5acd4e9678f8
Revises: 4a4804e1d242
Create Date: 2022-07-05 16:18:51.302823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5acd4e9678f8'
down_revision = '4a4804e1d242'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('videosLikes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('video_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['videos.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'video_id')
    )
    op.drop_table('vid_likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vid_likes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('video_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('is_liked', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='vid_likes_user_id_fkey'),
    sa.ForeignKeyConstraint(['video_id'], ['videos.id'], name='vid_likes_video_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='vid_likes_pkey')
    )
    op.drop_table('videosLikes')
    # ### end Alembic commands ###