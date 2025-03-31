from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram import types


start_router = Router()


@start_router.message(CommandStart())
async def handler_start(message: types.Message):
    # TODO запрос на FastAPI для добавления пользователя в БД
    kb = [types.KeyboardButton(text="Сгенерировать новый рецепт"),]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(
        f"Привет, {html.bold(html.quote(message.from_user.first_name))}! "
        "Я помогу придумать рецепт для твоего обеда, "
        "ужина, перекуса и другого любого приёма еды! "
        "Для старта нажмите на кнопку 'Сгенерировать новый рецепт'",
        reply_markup=keyboard
    )
