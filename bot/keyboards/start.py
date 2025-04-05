from aiogram import types


async def keyboard_for_new_user():
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="Сгенерировать новый рецепт")]],
        resize_keyboard=True,
    )
    return keyboard


async def keyboard_for_old_user():
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="Меню")]],
        resize_keyboard=True,
    )
    return keyboard
