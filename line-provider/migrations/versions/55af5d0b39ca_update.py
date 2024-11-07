"""update

Revision ID: 55af5d0b39ca
Revises: 841a2bd32dfc
Create Date: 2024-11-07 15:09:01.853502

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '55af5d0b39ca'
down_revision: Union[str, None] = '841a2bd32dfc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('events', 'id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('events', 'deadline',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=False)
    op.drop_index('ix_events_id', table_name='events')
    op.create_index(op.f('ix_events_id'), 'events', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_events_id'), table_name='events')
    op.create_index('ix_events_id', 'events', ['id'], unique=True)
    op.alter_column('events', 'deadline',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
    op.alter_column('events', 'id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###