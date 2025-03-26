from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class ShoppingList(Base):
    __tablename__ = "shopping_lists"

    id: Mapped[int] = mapped_column(
            Integer, primary_key=True, autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    ingredients: Mapped[list["Ingredient"]] = relationship(
        secondary="amount_ingredients",
        back_populates="shopping_lists",
    )

    user: Mapped["User"] = relationship(
        back_populates="shopping_list",
        uselist=False
    )
