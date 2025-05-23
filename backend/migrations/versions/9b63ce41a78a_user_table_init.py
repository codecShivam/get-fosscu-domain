"""user table init

Revision ID: 9b63ce41a78a
Revises: 
Create Date: 2024-12-12 01:54:23.991913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b63ce41a78a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('email_verified', sa.DateTime(), nullable=True),
    sa.Column('provider', sa.Enum('GITHUB', 'CUSTOM', name='provider'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
