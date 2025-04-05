from aiogram import F, Router, html
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram import types

common_router = Router()


@common_router.message(CommandStart())
async def handler_start(message: types.Message):
    # TODO запрос на добавление пользователя в БД
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
    # TODO если пользователь существует, приветствовать иначе


@common_router.message(StateFilter(None), Command(commands=["cancel"]))
@common_router.message(default_state, F.text.lower() == "отмена")
async def cmd_cancel_no_state(message: types.Message, state: FSMContext):
    await state.set_data({})
    await message.answer(
        text="Нечего отменять",
        reply_markup=types.ReplyKeyboardRemove()
    )


@common_router.message(Command(commands=["cancel"]))
@common_router.message(F.text.lower() == "отмена")
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=types.ReplyKeyboardRemove()
    )
