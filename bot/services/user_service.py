import logging

from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from bot.models.user import User, Project
from bot.utils.generators import generate_id


logger = logging.getLogger(__name__)


async def get_user_by_id(session: AsyncSession, user_id: str) -> Optional[User]:
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)

    return result.scalars().first()


async def get_project_by_owner_id(session: AsyncSession, owner_id: string) -> Optional[Project]:
    stmt = select(Project).where(Project.owner_id == owner_id)
    result = await session.execute(stmt)

    return result.scalars().first()


async def delete_user_by_id(session: AsyncSession, user_id: str) -> bool:
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)
    user = result.scalars().first()
    if user:
        await session.delete(user)
        logger.debug(f"Deleted member with ID {user_id}.")
        return True

    logger.debug(f"Member with ID {user_id} not found.")
    return False


async def create_user(session: AsyncSession, user_name: str, password: str) -> str:
    # logger.debug("create user")

    id = await generate_id(session)

    # async with db_session:
    new_user = User(
        id=id,
        user_name=user_name,
        password=password,
        projects=None
        )
    logger.debug(f"created {new_user}")
    session.add(new_user)
    await session.flush()
    # await session.refresh(new_room)
    logger.debug(f"Added to database {new_user}")
    # await session.commit()

    return id


async def add_project(session: AsyncSession, project_name: str, owner_id: str) -> bool:
    user = await get_user_by_id(session, owner_id)

    if user:
        new_project = Project(owner_id=owner_id, project_name=project_name)
        user.projects.append(new_project)
        # await session.commit()
        logger.debug(f"Added to database {new_project}")

        return True

    return False
