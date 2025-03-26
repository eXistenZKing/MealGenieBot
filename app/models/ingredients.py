from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(
            Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    measurement_unit: Mapped[str] = mapped_column(String(20), nullable=False)

    shopping_lists: Mapped[list["ShoppingList"]] = relationship(
        secondary="amount_ingredients",
        back_populates="ingredients"
    )
