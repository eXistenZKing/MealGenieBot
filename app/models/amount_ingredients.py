from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class AmountIngredient(Base):
    __tablename__ = "amount_ingredients"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.id"))
    amount: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    shopping_list_id: Mapped[int] = mapped_column(
        ForeignKey("shopping_lists.id")
    )

    shopping_list: Mapped["ShoppingList"] = relationship(
        back_populates="amount_ingredients"
    )
    ingredient: Mapped["Ingredient"] = relationship(
        back_populates="amount_ingredients"
    )
