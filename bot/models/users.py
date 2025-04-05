from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.core.database import Base


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

    shopping_list: Mapped["ShoppingList"] = relationship(
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )
