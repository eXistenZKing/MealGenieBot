from aiogram import types


async def number_of_recipes_keyboard():
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="1 рецепт",
                    callback_data="cooking_time"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="2 рецепта",
                    callback_data="cooking_time"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="3 рецепта",
                    callback_data="cooking_time"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Отмена",
                    callback_data="cancel"
                )
            ]
        ]
    )
    return keyboard


async def cooking_time_keyboard():
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="15-30 минут",
                    callback_data="type_of_cooking"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="30-60 минут",
                    callback_data="type_of_cooking"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="60+ минут",
                    callback_data="type_of_cooking"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Назад",
                    callback_data="back_to_recipes"
                ),
                types.InlineKeyboardButton(
                    text="Отмена",
                    callback_data="cancel"
                )
            ]
        ]
    )
    return keyboard


async def type_of_cooking_keyboard():
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Жарка",
                    callback_data="generate_recipes"
                ),
                types.InlineKeyboardButton(
                    text="Варка",
                    callback_data="generate_recipes"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Запекание",
                    callback_data="generate_recipes"
                ),
                types.InlineKeyboardButton(
                    text="Тушение",
                    callback_data="generate_recipes"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Назад",
                    callback_data="back_to_time"
                ),
                types.InlineKeyboardButton(
                    text="Отмена",
                    callback_data="cancel"
                )
            ]
        ]
    )
    return keyboard
