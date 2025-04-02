from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    telegram_id: str
    language: str = Field("ru", max_length=2)
