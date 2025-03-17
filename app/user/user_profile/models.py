from typing import Optional

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class UserProfile(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
