from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
import asyncio
from typing import Any, Awaitable, Callable, Dict

from bot.config import settings
from bot.core.ai_client import AIClient
from bot.core.database import database
from bot.handlers import common_router, maintenance_router, recipe_router


bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(maintenance_mode=settings.maintenance_mode)
dp.callback_query.middleware(CallbackAnswerMiddleware())

# Инициализация AI клиента
ai_client = AIClient(api_key=settings.OPENAI_API_KEY)


# Middleware для внедрения сессии
async def db_session_middleware(
    handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
    event: Any,
    data: Dict[str, Any]
) -> Any:
    session = await database.async_session()
    data["session"] = session
    try:
        return await handler(event, data)
    finally:
        await session.close()


async def main():
    dp["ai_client"] = ai_client
    dp.update.outer_middleware(db_session_middleware)
    dp.include_routers(maintenance_router, recipe_router, common_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
