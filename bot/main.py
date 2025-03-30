from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio

from config import settings
from bot.handlers import start_router


bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


async def main():
    dp.include_router(start_router)
    await dp.start_polling(bot)


# async def set_webhook():
#     await bot.set_webhook(
#         url="http://backend:8000/webhook",
#     )


if __name__ == "__main__":
    asyncio.run(main())
