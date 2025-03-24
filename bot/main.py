from aiogram import Bot
import asyncio

from config import settings


async def main():
    bot = Bot(token=settings.BOT_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
