from aiogram.fsm.state import State, StatesGroup


class RecipeGenerate(StatesGroup):
    choosing_number_recipes = State()
    choosing_cooking_time = State()
    choosing_cooking_type = State()
