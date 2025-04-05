from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from bot.core.database import Base


class Language(Base):
    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    code: Mapped[str] = mapped_column(String(2), unique=True)
    public_name: Mapped[str] = mapped_column(String(50), unique=True)
