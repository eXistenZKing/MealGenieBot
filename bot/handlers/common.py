from aiogram import F, Router, html, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from bot.fsm import RecipeGenerate
from bot.keyboards import (
    keyboard_for_old_user,
    keyboard_for_new_user,
    keyboard_for_menu
)
from bot.crud.users import create_new_user

common_router = Router()


@common_router.message(CommandStart())
async def handler_start(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession
):
    is_new_user = await create_new_user(
        session=session,
        telegram_id=message.from_user.id
    )
    user_name = html.bold(html.quote(message.from_user.first_name))
    if is_new_user:
        await message.answer(
            f"Привет, {user_name}! "
            "Я помогу придумать рецепт для твоего обеда, "
            "ужина, перекуса и другого любого приёма еды! "
            "Для старта нажмите на кнопку 'Сгенерировать новый рецепт'",
            reply_markup=await keyboard_for_new_user()
        )
        await state.set_state(RecipeGenerate.choosing_number_recipes)
    else:
        user_name = html.bold(html.quote(message.from_user.first_name))
        welcome_text = (
            f"С возвращением, {user_name}! "
            "Рад видеть вас снова! "
            "Вы можете сгенерировать новый рецепт или "
            "воспользоваться дополнительными функциями в меню."
        )
        await message.answer(
            welcome_text,
            reply_markup=await keyboard_for_old_user()
        )


@common_router.message(F.text == "Меню")
async def show_menu(message: types.Message):
    await message.answer(
        "Выберите действие:",
        reply_markup=await keyboard_for_menu()
    )


@common_router.callback_query(F.data == "cancel")
async def cmd_cancel(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer()
    await callback.message.answer(
        text="Действие отменено. Выберите новое действие в меню: ",
        reply_markup=await keyboard_for_menu()
    )
