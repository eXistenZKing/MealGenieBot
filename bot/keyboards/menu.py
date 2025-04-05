from aiogram import types


async def keyboard_for_menu():
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Сгенерировать новый рецепт")],
            [types.KeyboardButton(text="Посмотреть рецепты")],
            [types.KeyboardButton(text="Посмотреть список покупок")],
            [types.KeyboardButton(text="Посмотреть список избранного")],

        ],
        resize_keyboard=True,
    )
    return keyboard
