"""fix_db_user_autoincrement_true

Revision ID: dd86c57da840
Revises: ecc2ef65d4f6
Create Date: 2025-03-11 16:20:32.162877

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dd86c57da840"
down_revision: Union[str, None] = "ecc2ef65d4f6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
