from sqlalchemy import (
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    UniqueConstraint
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.core.database import Base
from bot.models.users import User


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(100), unique=True)
    unit: Mapped[str] = mapped_column(String(20))

    amount_ingredients: Mapped[list["AmountIngredient"]] = relationship(
        back_populates="ingredient",
        overlaps="shopping_lists"
    )
    shopping_lists: Mapped[list["ShoppingList"]] = relationship(
        secondary="amount_ingredients",
        back_populates="ingredients",
        overlaps="amount_ingredients"
    )

    __table_args__ = (
        UniqueConstraint(
            "name", "unit", name="uq_ingredient_measurement"),
    )


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
        back_populates="amount_ingredients",
        overlaps="ingredients,shopping_lists"
    )
    ingredient: Mapped["Ingredient"] = relationship(
        back_populates="amount_ingredients",
        overlaps="shopping_lists"
    )

    __table_args__ = (
        UniqueConstraint(
            "ingredient_id", "shopping_list_id", name="uq_ingr_shop_cart"),
        Index("ix_ingr_shop_cart_ingredient_id", "ingredient_id"),
        Index("ix_ingr_shop_cart_shopping_list_id", "shopping_list_id"),
    )


class ShoppingList(Base):
    __tablename__ = "shopping_lists"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    amount_ingredients: Mapped[list["AmountIngredient"]] = relationship(
        back_populates="shopping_list",
        overlaps="ingredients"
    )
    ingredients: Mapped[list["Ingredient"]] = relationship(
        secondary="amount_ingredients",
        back_populates="shopping_lists",
        overlaps="amount_ingredients,ingredient"
    )
    user: Mapped[User] = relationship(
        back_populates="shopping_list",
        uselist=False
    )
