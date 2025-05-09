import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot.keyboards.inline import confirm_kb
from bot.template_engine import template_engine
from bot.middlewares.resourses_middleware import ResourcesMiddleware

from sqlalchemy.ext.asyncio import AsyncSession

user_router = Router()
# user_router.message.middleware(ResourcesMiddleware())  # adding middleware for messages to this router
# user_router.callback_query.middleware(ResourcesMiddleware())  # adding middleware for callback to this router
logger = logging.getLogger(__name__)

