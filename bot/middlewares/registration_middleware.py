import logging

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
# from cachetools import TTLCache

from bot.services.registration_service import AuthService

# Импортируем вашу модель пользователя
from bot.models.user import User

# Кэш для хранения проверенных пользователей (опционально)
# user_cache = TTLCache(maxsize=10_000, ttl=300)  # 10k записей, 5 минут жизни

class RegistrationMiddleware(BaseMiddleware):
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        # Проверяем только сообщения (можно добавить другие типы событий)
        if not isinstance(event, types.Message):
            return await handler(event, data)

        # Получаем сессию из data (созданную ResourcesMiddleware)
        db_session: AsyncSession = data["db_session"]
        user_id = event.from_user.id  # obtaining user id
        auth = AuthService(db_session)

        # Проверяем кэш (опционально)
        # if user_id in user_cache:
        #     return await handler(event, data)

        # Проверяем наличие пользователя в БД
        # stmt = select(User).where(User.id == user_id)
        # result = await session.execute(stmt)
        # user = await db_session.execute(
        #     select(User).where(User.id == user_id)
        # )
        # user = user.scalar_one_or_none()

        if not await auth.is_registered(user_id):
            # starting registration process
            # await event.answer("❌ Вы не зарегистрированы! Пожалуйста, используйте /start")
            await db_session.close()  # Явно закрываем сессию, так как handler не будет вызван

            return  # Прерываем цепочку middleware

        # Сохраняем в кэш (опционально)
        # user_cache[user_id] = True

        # Продолжаем выполнение
        return await handler(event, data)