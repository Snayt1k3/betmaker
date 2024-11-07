"""update

Revision ID: c324b728c2c4
Revises: 55af5d0b39ca
Create Date: 2024-11-07 15:12:31.880784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c324b728c2c4'
down_revision: Union[str, None] = '55af5d0b39ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SEQUENCE IF NOT EXISTS events_id_seq")
    op.execute("ALTER TABLE events ALTER COLUMN id SET DEFAULT nextval('events_id_seq')")
    op.execute("ALTER SEQUENCE events_id_seq OWNED BY events.id")
    # ### end Alembic commands ###


def downgrade():
    # Удаление последовательности
    op.execute("ALTER TABLE events ALTER COLUMN id DROP DEFAULT")
    op.execute("DROP SEQUENCE IF EXISTS events_id_seq")