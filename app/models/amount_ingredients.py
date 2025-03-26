from sqlalchemy import Float, ForeignKey, Integer, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class AmountIngredient(Base):
    __tablename__ = "amount_ingredients"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.id"))
    amount: Mapped[float] = mapped_column(Float, default=1, nullable=False)
    shopping_list_id: Mapped[int] = mapped_column(
        ForeignKey("shopping_lists.id")
    )

    shopping_list: Mapped["ShoppingList"] = relationship(
        "ShoppingList",
        back_populates="amount_ingredients"
    )
    ingredient: Mapped["Ingredient"] = relationship(
        "Ingredient",
        back_populates="amount_ingredients"
    )

    __table_args__ = (
        UniqueConstraint(
            "ingredient_id", "shopping_list_id", name="uq_ingr_shop_cart"),
        Index("ix_ingr_shop_cart_ingredient_id", "ingredient_id"),
        Index("ix_ingr_shop_cart_shopping_list_id", "shopping_list_id"),
    )
