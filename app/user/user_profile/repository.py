from dataclasses import dataclass
from typing import Optional
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.exception import UserAlreadyExists
from app.user.user_profile.models import UserProfile
from app.user.user_profile.schema import CreateUser


@dataclass
class UserRepository:
    db_session: AsyncSession

    async def create_user(self, user: CreateUser) -> UserProfile:
        query = (
            insert(UserProfile).values(**user.model_dump()).returning(UserProfile.id)
        )
        async with self.db_session as session:
            try:
                result = await session.execute(query)
                user_id = result.scalar_one()
                await session.commit()
            except IntegrityError as e:
                await session.rollback()
                raise UserAlreadyExists(
                    f"Пользователь с именем {user.username} уже существует"
                ) from e
            return await self.get_user(user_id)

    async def get_user(self, user_id) -> Optional[UserProfile]:
        query = select(UserProfile).where(UserProfile.id == user_id)
        async with self.db_session as session:
            result = await session.execute(query)
            return result.scalars().first()

    async def get_user_by_username(self, username: str) -> Optional[UserProfile]:
        query = select(UserProfile).where(UserProfile.username == username)
        async with self.db_session as session:
            result = await session.execute(query)
            return result.scalars().first()
