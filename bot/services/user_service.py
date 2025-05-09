import logging

from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from bot.models.user import User, Project
from bot.utils.generators import generate_id


logger = logging.getLogger(__name__)


async def get_user_by_id(session: AsyncSession, user_id: str) -> Optional[User]:
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)

    return result.scalars().first()


async def get_projects_by_owner_id(session: AsyncSession, owner_id: id) -> Optional[List[Project]]:
    stmt = select(Project).where(Project.owner_id == owner_id)
    result = await session.execute(stmt)

    return result.scalars()


async def get_project_by_id(session: AsyncSession, project_id: id) -> Optional[Project]:
    stmt = select(Project).where(Project.id == project_id)
    result = await session.execute(stmt)

    return result.scalars().first()


async def delete_user_by_id(session: AsyncSession, user_id: int) -> bool:
    stmt = select(User).where(User.id == user_id)  # searching objects that fit prompt
    result = await session.execute(stmt)
    user = result.scalars().first()
    if user:
        await session.delete(user)
        logger.debug(f"Deleted member with ID {user_id}.")
        return True

    logger.debug(f"Member with ID {user_id} not found.")
    return False


async def add_project(session: AsyncSession, owner_id: str, project_name: str) -> Optional[str]:
    user = await get_user_by_id(session, owner_id)
    id = await generate_id(session)

    if user:
        new_project = Project(id=id, owner_id=owner_id, project_name=project_name)
        user.projects.append(new_project)
        await session.flush()  # Synchronize data with the database without closing the session
        logger.debug(f"Added to database {new_project}")

        return id

    return None
