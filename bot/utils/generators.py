import string
import random

from sqlalchemy.ext.asyncio import AsyncSession

from bot.services.user_service import get_user_by_id


async def generate_id(session: AsyncSession, length=5):
    characters = string.ascii_uppercase + string.digits

    while True:
        id = ''.join(random.choice(characters) for _ in range(length))
        if not await get_user_by_id(session, id):
            return id