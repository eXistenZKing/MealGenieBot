from pydantic import BaseModel


class RecipeRequest(BaseModel):
    number_of_recipes: str
    cooking_time: str
    cooking_type: str
