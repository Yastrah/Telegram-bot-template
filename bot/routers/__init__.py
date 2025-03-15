from aiogram import Dispatcher

from .commands import commands_router
from .form import form_router

def include_all_routers(dp: Dispatcher) -> None:
    """
    Including all routers in Dispatcher
    """
    dp.include_router(commands_router)
    dp.include_router(form_router)