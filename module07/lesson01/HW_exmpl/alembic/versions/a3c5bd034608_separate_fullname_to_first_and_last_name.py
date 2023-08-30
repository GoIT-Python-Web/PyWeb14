"""separate fullname to first and last name

Revision ID: a3c5bd034608
Revises: 2f508046c896
Create Date: 2023-08-30 20:22:21.791615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3c5bd034608'
down_revision: Union[str, None] = '2f508046c896'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('first_name', sa.String(length=250), nullable=True))
    op.add_column('students', sa.Column('last_name', sa.String(length=250), nullable=True))
    op.drop_column('students', 'fullname')
    op.add_column('tutors', sa.Column('first_name', sa.String(length=250), nullable=True))
    op.add_column('tutors', sa.Column('last_name', sa.String(length=250), nullable=True))
    op.drop_column('tutors', 'fullname')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tutors', sa.Column('fullname', sa.VARCHAR(length=250), nullable=False))
    op.drop_column('tutors', 'last_name')
    op.drop_column('tutors', 'first_name')
    op.add_column('students', sa.Column('fullname', sa.VARCHAR(length=250), nullable=False))
    op.drop_column('students', 'last_name')
    op.drop_column('students', 'first_name')
    # ### end Alembic commands ###