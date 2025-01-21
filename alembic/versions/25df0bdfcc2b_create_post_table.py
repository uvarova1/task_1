"""create_post_table

Revision ID: 25df0bdfcc2b
Revises: 5ee3095bccb3
Create Date: 2025-01-21 10:51:47.508710

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25df0bdfcc2b'
down_revision: Union[str, None] = '5ee3095bccb3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='post_pkey')
    )
    # ### end Alembic commands ###
