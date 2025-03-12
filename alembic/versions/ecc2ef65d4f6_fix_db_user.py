"""fix_db_User

Revision ID: ecc2ef65d4f6
Revises: 1b077690ffe0
Create Date: 2025-03-11 15:52:59.000844

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ecc2ef65d4f6"
down_revision: Union[str, None] = "1b077690ffe0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f("ix_forms_id"), "forms", ["id"], unique=False)
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_index(op.f("ix_forms_id"), table_name="forms")
    # ### end Alembic commands ###
