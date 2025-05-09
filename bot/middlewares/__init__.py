from aiogram import Dispatcher

from .resourses_middleware import ResourcesMiddleware
from .registration_middleware import RegistrationMiddleware


def add_all_middlewares(dp: Dispatcher) -> None:
    """
    Adding all middlewares to Dispatcher
    """
    dp.update.middleware(ResourcesMiddleware())
    dp.update.middleware(RegistrationMiddleware())