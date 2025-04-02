from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import database
from app.crud import get_user
from app.schemas import User


async def get_current_user(
        request: Request,
        session: AsyncSession = Depends(database.async_session)) -> User:
    user = await get_user(session, request.get("id"))
    return user
