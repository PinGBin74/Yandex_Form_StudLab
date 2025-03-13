from dataclasses import dataclass
from typing import Optional
from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from exception import UserAlreadyExists
from models import UserProfile
from schema import CreateUser
from sqlalchemy.exc import IntegrityError
@dataclass
class UserRepository:
    db_session: Session

    def create_user(self, user: CreateUser) -> UserProfile:
        query = insert(UserProfile).values(**user.model_dump()).returning(UserProfile.id)
        with self.db_session() as session:
            try:
                user_id: int = session.execute(query).scalar()
                session.commit()
            except IntegrityError as e:
                session.rollback()
                raise UserAlreadyExists(f"Пользователь с именем {user.username} уже существует") from e
            session.flush()
            return self.get_user(user_id)
    def get_user(self, user_id) -> Optional[UserProfile]:
        query = select(UserProfile).where(UserProfile.id == user_id)
        with self.db_session() as session:
            return session.execute(query).scalars().first()

    def get_user_by_username(self, username: str) -> Optional[UserProfile]:
        query = select(UserProfile).where(UserProfile.username == username)
        with self.db_session() as session:
            return session.execute(query).scalars().first()
