from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class ShoppingList(Base):
    __tablename__ = "shopping_lists"

    id: Mapped[int] = mapped_column(
            Integer, primary_key=True, autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    amount_ingredients: Mapped[list["AmountIngredient"]] = relationship(
        back_populates="shopping_list",
        cascade="all, delete-orphan"
    )
