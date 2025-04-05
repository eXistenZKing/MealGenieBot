from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot.models import User
from bot.schemas.users import User as UserSchema


async def create_new_user(
        session: AsyncSession, telegram_id: int) -> bool | None:
    user_data = UserSchema(telegram_id=telegram_id)
    try:
        query = await session.execute(
            select(User).filter_by(telegram_id=user_data.telegram_id)
        )
        user = query.scalar_one_or_none()
        if not user:
            new_user = User(**user_data.model_dump())
            session.add(new_user)
            await session.commit()
            return True
        return False
    except Exception as e:
        await session.rollback()
        print(f"Error occurred while creating user: {e}")


async def get_user(session: AsyncSession, telegram_id: int) -> User | None:
    query = await session.execute(
        select(User).filter_by(telegram_id=str(telegram_id))
    )
    user = query.scalar_one_or_none()
    return user
