import logging

from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from bot.models.user import User, Project
from bot.utils.generators import generate_id


logger = logging.getLogger(__name__)


class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self._logger = logging.getLogger(__name__)

    async def register_user(self, telegram_id: int, user_name: str, password: str) -> User:
        user = User(
            id=telegram_id,
            user_name=user_name,
            password=password,
            projects=None
        )
        self.session.add(user)
        await self.session.flush()  # Synchronize data with the database without closing the session
        self._logger.debug(f"Added to database {user}")
        return user

    async def is_registered(self, telegram_id: int) -> bool:
        result = await self.session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none() is not None