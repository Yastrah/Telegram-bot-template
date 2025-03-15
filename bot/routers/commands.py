import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.reply import yes_no_kb
from bot.template_engine import template_engine
from bot.config import settings
from bot.states import Form
from bot.middlewares.resourses_middleware import ResourcesMiddleware

from sqlalchemy.ext.asyncio import AsyncSession


commands_router = Router()
commands_router.message.middleware(ResourcesMiddleware())

logger = logging.getLogger(__name__)


@commands_router.message(Command("start"))
@commands_router.message(F.text.casefold() == "start")
async def cmd_start(message: Message, state: FSMContext, db_session: AsyncSession):
    await state.set_state(Form.idea)

    await message.answer(template_engine.render_template(
        "start",
        user_name=message.from_user.username,
        bot_name=settings.bot.idea
    ),
        reply_markup=yes_no_kb())
    logger.debug(f"Sent answer for /start command to user {message.from_user.username}")
