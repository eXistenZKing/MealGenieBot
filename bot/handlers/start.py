from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


start_router = Router()


@start_router.message(CommandStart())
async def handler_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! "
        "Я помогу придумать рецепт для твоего обеда, "
        "ужина, перекуса и другого любого приёма еды! "
        "Выбери желаемое количество рецептов, "
        "которое я сгенерирую по твои параметрам:"
    )
    # TODO запрос на FastAPI для добавления пользователя в БД
