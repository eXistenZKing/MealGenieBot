from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from bot.core.database import database
from bot.crud import get_user
from bot.schemas import User


async def get_current_user(
        request: Request,
        session: AsyncSession = Depends(database.async_session)) -> User:
    user = await get_user(session, request.get("id"))
    return user
