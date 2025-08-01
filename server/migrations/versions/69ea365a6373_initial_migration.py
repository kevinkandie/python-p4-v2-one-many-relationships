"""initial migration

Revision ID: 69ea365a6373
Revises: 406e9095a629
Create Date: 2025-05-18 15:00:50.862976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69ea365a6373'
down_revision = '406e9095a629'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('content', sa.String(), nullable=True))
    op.drop_column('reviews', 'summary')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('summary', sa.VARCHAR(), nullable=True))
    op.drop_column('reviews', 'content')
    # ### end Alembic commands ###
