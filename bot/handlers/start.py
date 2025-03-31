from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


start_router = Router()


@start_router.message(CommandStart())
async def handler_start(message: types.Message):
    # TODO запрос на FastAPI для добавления пользователя в БД
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="1",
        callback_data="cooking_time")
    )
    builder.add(types.InlineKeyboardButton(
        text="2",
        callback_data="cooking_time")
    )
    builder.add(types.InlineKeyboardButton(
        text="3",
        callback_data="cooking_time")
    )
    await message.answer(
        f"Привет, {html.bold(html.quote(message.from_user.first_name))}! "
        "Я помогу придумать рецепт для твоего обеда, "
        "ужина, перекуса и другого любого приёма еды! "
        "Выбери желаемое количество рецептов, "
        "которое я сгенерирую по твои параметрам:",
        reply_markup=builder.as_markup()
    )
