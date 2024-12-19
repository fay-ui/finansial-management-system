"""
Revision ID: 12345abcde
Revises: 98765zyxwv
Create Date: 2024-12-19 10:00:00
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "12345abcde"
down_revision: Union[str, None] = "98765zyxwv"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Example: create a new table
    op.create_table(
        'new_table',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False)
    )

    # Example: add a column to an existing table
    op.add_column('existing_table', sa.Column('new_column', sa.Integer(), nullable=True))


def downgrade() -> None:
    # Example: drop the new table if rolling back
    op.drop_table('new_table')

    # Example: remove the column from the existing table if rolling back
    op.drop_column('existing_table', 'new_column')
