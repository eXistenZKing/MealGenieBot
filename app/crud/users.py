from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User, ShoppingList


async def create_new_user(
        session: AsyncSession, telegram_id: int) -> bool | None:
    try:
        query = await session.execute(
            select(User).filter_by(telegram_id=telegram_id)
        )
        user = query.scalar_one_or_none()
        if not user:
            new_user = User(telegram_id=telegram_id)
            session.add(new_user)
            await session.flush()
            new_user_shopping_list = ShoppingList(user_id=new_user.id)
            session.add(new_user_shopping_list)
            await session.commit()
            return True
        return False
    except Exception as e:
        await session.rollback()
        print(f"Error occurred while creating user: {e}")
