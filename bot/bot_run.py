from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
import asyncio

from bot.config import settings
from bot.handlers import maintenance_router, recipe_router, start_router


bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(maintenance_mode=settings.maintenance_mode)
dp.callback_query.middleware(CallbackAnswerMiddleware())


async def main():
    dp.include_router(maintenance_router, recipe_router, start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# async def set_webhook():
#     await bot.set_webhook(
#         url="http://backend:8000/webhook",
#     )


if __name__ == "__main__":
    asyncio.run(main())
