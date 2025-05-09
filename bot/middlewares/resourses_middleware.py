import logging

from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession

from bot.services.database import engine


class ResourcesMiddleware(BaseMiddleware):
    def __init__(self):
        """
        Initializes self
        """
        self._logger = logging.getLogger(__name__)


    async def _cleanup(self, data: dict):
        """
        Closes connections & etc.
        :param data:
        :return:
        """

        # self._logger.debug("Cleaning resources")

        if "db_session" in data:
            # self._logger.debug("SQLAlchemy session detected, closing connection.")
            session: AsyncSession = data["db_session"]
            await session.commit()  # Commit changes
            await session.close()


    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        # self._logger.debug("Before handler")
        data["db_session"] = AsyncSession(engine)

        result = await handler(event, data)

        # If you make a return in the handler, then this value will go to result

        # self._logger.debug("After handler")
        await self._cleanup(data)
        return result
