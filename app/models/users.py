from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    telegram_id: Mapped[str] = mapped_column(
        String, unique=True, nullable=False
    )
    language: Mapped[str] = mapped_column(
        ForeignKey("languages.code"), default="ru"
    )
