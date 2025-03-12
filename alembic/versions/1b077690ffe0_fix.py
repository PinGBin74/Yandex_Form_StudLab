"""Fix index issue

Revision ID: 1b077690ffe0
Revises: 996ac0dfc6d6
Create Date: 2023-10-10 12:00:00.000000

"""

from alembic import op
import sqlalchemy as sa

# Идентификаторы ревизий
revision = "1b077690ffe0"
down_revision = "996ac0dfc6d6"
branch_labels = None
depends_on = None


def upgrade():
    # Получаем инспектор для проверки состояния базы данных
    inspector = sa.inspect(op.get_bind())

    # Получаем список всех индексов для таблицы 'users'
    indexes = inspector.get_indexes("users")

    # Проверяем, существует ли индекс 'ix_users_id'
    if any(index["name"] == "ix_users_id" for index in indexes):
        # Если индекс существует, удаляем его
        op.drop_index("ix_users_id", table_name="users")


def downgrade():
    # Восстанавливаем индекс (если нужно)
    op.create_index("ix_users_id", "users", ["id"], unique=False)
