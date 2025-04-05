from openai import AsyncOpenAI

from bot.schemas import RecipeRequest


class AIClient:
    def __init__(self, api_key: str):
        self.client = AsyncOpenAI(api_key=api_key)

    async def generate_recipe(self, request: RecipeRequest) -> str:
        system_prompt = (
            "Ты - опытный шеф-повар. Твоя задача - генерировать рецепты "
            "на русском языке. Рецепт должен быть подробным, с указанием "
            "времени приготовления, "
            "списком ингредиентов и пошаговой инструкцией."
        )

        user_prompt = (
            f"Сгенерируй {request.number_of_recipes} рецепт(ов) с временем "
            f"приготовления {request.cooking_time}. "
            f"Тип приготовления: {request.cooking_type}. "
            "Формат ответа:\n"
            "# Название блюда\n"
            "Время приготовления: X минут\n"
            "## Ингредиенты:\n"
            "- ингредиент 1\n"
            "- ингредиент 2\n"
            "## Инструкция:\n"
            "1. Шаг 1\n"
            "2. Шаг 2"
        )

        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )

        return response.choices[0].message.content
