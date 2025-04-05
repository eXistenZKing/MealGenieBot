from aiogram import Bot, F, Router, types
from aiogram.fsm.context import FSMContext

from bot.core.ai_client import AIClient, RecipeRequest
from bot.fsm import RecipeGenerate
from bot.keyboards import (
    cooking_time_keyboard,
    type_of_cooking_keyboard,
    number_of_recipes_keyboard
)


recipe_router = Router()


@recipe_router.message(
        RecipeGenerate.choosing_number_recipes,
        F.text == "Сгенерировать новый рецепт")
async def number_of_recipes(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Выберите желаемое количество рецептов, "
        "которое вы хотите сгенерировать:",
        reply_markup=await number_of_recipes_keyboard()
    )
    await state.set_state(RecipeGenerate.choosing_cooking_time)


@recipe_router.callback_query(
        RecipeGenerate.choosing_cooking_time,
        F.data == "cooking_time")
async def cooking_time(callback: types.CallbackQuery, state: FSMContext):
    number = callback.message.reply_markup.inline_keyboard[0][0].text
    await state.update_data(number_of_recipes=number)
    await callback.answer()

    await callback.message.delete()

    await callback.message.answer(
        "Отлично! Выберите желаемое время, "
        "которое вы хотите потратить на приготовление:",
        reply_markup=await cooking_time_keyboard()
    )
    await state.set_state(RecipeGenerate.choosing_cooking_type)


@recipe_router.callback_query(
        RecipeGenerate.choosing_cooking_type,
        F.data == "type_of_cooking")
async def type_of_cooking(callback: types.CallbackQuery, state: FSMContext):
    cooking_time = callback.message.reply_markup.inline_keyboard[0][0].text
    await state.update_data(cooking_time=cooking_time)
    await callback.answer()

    await callback.message.delete()

    await callback.message.answer(
        "И последнее, выберите желаемый тип приготовления:",
        reply_markup=await type_of_cooking_keyboard()
    )


@recipe_router.callback_query(F.data == "back_to_recipes")
async def back_to_recipes(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer(
        "Выберите желаемое количество рецептов, "
        "которое вы хотите сгенерировать:",
        reply_markup=await number_of_recipes_keyboard()
    )
    await state.set_state(RecipeGenerate.choosing_cooking_time)


@recipe_router.callback_query(F.data == "back_to_time")
async def back_to_time(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer(
        "Выберите желаемое время, "
        "которое вы хотите потратить на приготовление:",
        reply_markup=await cooking_time_keyboard()
    )
    await state.set_state(RecipeGenerate.choosing_cooking_type)


@recipe_router.callback_query(F.data == "generate_recipes")
async def generate_recipes(
    callback: types.CallbackQuery,
    bot: Bot,
    state: FSMContext,
    ai_client: AIClient
):
    chat_id = callback.message.chat.id
    await bot.send_chat_action(chat_id, "typing")

    cooking_type = callback.message.reply_markup.inline_keyboard[0][0].text

    await callback.message.delete()

    await state.update_data(cooking_type=cooking_type)
    await callback.answer()

    user_data = await state.get_data()
    print(f"Collected data: {user_data}")

    request = RecipeRequest(
        number_of_recipes=user_data["number_of_recipes"],
        cooking_time=user_data["cooking_time"],
        cooking_type=user_data["cooking_type"]
    )

    try:
        recipe_text = await ai_client.generate_recipe(request)
        await callback.message.answer(recipe_text, parse_mode="Markdown")
    except Exception as e:
        await callback.message.answer(
            "Извините, произошла ошибка при генерации рецепта. "
            "Пожалуйста, попробуйте еще раз."
        )
        print(f"Error generating recipe: {e}")

    await state.clear()
