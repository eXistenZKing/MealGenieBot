from pydantic import BaseModel, Field, field_validator


class User(BaseModel):
    telegram_id: str
    language: str = Field("ru", max_length=2)

    @field_validator("telegram_id", mode="before")
    def convert_to_str(cls, value):
        return str(value)
