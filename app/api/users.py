from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import create_new_user
from app.core.database import database


router = APIRouter(prefix="/users")


@router.post("/")
async def create_user(
    telegram_id: int,
    session: AsyncSession = Depends(database.async_session)
) -> bool | None:
    result = await create_new_user(session, telegram_id)
    return result
