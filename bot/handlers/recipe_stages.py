from aiogram import Bot, F, Router, html, types
from aiogram.utils.keyboard import InlineKeyboardBuilder


recipe_router = Router()


@recipe_router.callback_query(F.data == "cooking_time")
async def cooking_time(callback: types.CallbackQuery):
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


@recipe_router.callback_query(F.data == "type_of_cooking")
async def type_of_cooking(callback: types.CallbackQuery):
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


@recipe_router.callback_query(F.data == "generate_recipes")
async def generate_recipes(callback: types.CallbackQuery, bot: Bot):
    await bot.send_chat_action(callback.chat.id, types.ChatActions.TYPING)
    # TODO вызов FastAPI для геренации рецепта
    # и отпавка его (их) пользователю в разметке HTML
