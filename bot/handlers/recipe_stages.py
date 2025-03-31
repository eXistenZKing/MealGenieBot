from aiogram import Bot, F, Router, html, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.fsm import RecipeGenerate


recipe_router = Router()


@recipe_router.message(
        StateFilter(None),
        F.text == "Сгенерировать новый рецепт")
async def number_of_recipes(message: types.Message, state: FSMContext):
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
        "Выберите желаемое время, "
        "котороев вы хотите потратить на приготовление",
        reply_markup=builder.as_markup()
    )
    await state.set_state(RecipeGenerate.choosing_cooking_time)


@recipe_router.callback_query(
        RecipeGenerate.choosing_number_recipes,
        F.data == "cooking_time")
async def cooking_time(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="5-20 минут",
        callback_data="type_of_cooking")
    )
    builder.add(types.InlineKeyboardButton(
        text="До одного часа",
        callback_data="type_of_cooking")
    )
    builder.add(types.InlineKeyboardButton(
        text="Свыше одного часа",
        callback_data="type_of_cooking")
    )
    await callback.message.answer(
        "Отлично! Выберите желаемое время, "
        "котороев вы хотите потратить на приготовление",
        reply_markup=builder.as_markup()
    )
    await state.set_state(RecipeGenerate.choosing_cooking_time)


@recipe_router.callback_query(
        RecipeGenerate.choosing_cooking_time,
        F.data == "type_of_cooking")
async def type_of_cooking(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Запечь в духовке",
        callback_data="generate_recipes")
    )
    builder.add(types.InlineKeyboardButton(
        text="Использовать плиту (например, кастрюлю, сковородку)",
        callback_data="generate_recipes")
    )
    builder.add(types.InlineKeyboardButton(
        text="Неважно",
        callback_data="generate_recipes")
    )
    await callback.message.answer(
        "И последнее, выберите желаемый тип приготовления",
        reply_markup=builder.as_markup()
    )
    await state.set_state(RecipeGenerate.choosing_cooking_type)


@recipe_router.callback_query(F.data == "generate_recipes")
async def generate_recipes(callback: types.CallbackQuery,
                           bot: Bot,
                           state: FSMContext):
    await bot.send_chat_action(callback.chat.id, types.ChatActions.TYPING)
    # TODO вызов FastAPI для геренации рецепта
    # и отпавка его (их) пользователю в разметке HTML
    await state.clear()
