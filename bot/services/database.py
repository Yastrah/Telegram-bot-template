import logging
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

# from bot.services.base import Base


logger = logging.getLogger(__name__)
DATABASE_URL = "sqlite+aiosqlite:///data/database.db"


Base = declarative_base()
engine = create_async_engine(DATABASE_URL)
# async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)  # delete data and tables
        await conn.run_sync(Base.metadata.create_all)  # creates tables with model Base


# # Example usage: Adding a new user
# async def add_user(name, age):
#     async with async_session() as session:
#         async with session.begin():
#             new_user = User(name=name, age=age)
#             session.add(new_user)
#             await session.commit()
#             print(f"Added user: {new_user}")
#
# # Example usage: Querying users
# async def get_users():
#     async with async_session() as session:
#         # result = await session.execute(text("SELECT * FROM users"))
#         # result.fetchall()
#         result = await session.execute(select(User))
#         users = result.scalars().all()
#         # users = result.scalars().first()
#
#         for user in users:
#             print(user)
#

