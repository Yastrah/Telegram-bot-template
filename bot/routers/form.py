import logging

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    ReplyKeyboardRemove,  # clear keyboards
)

from bot.keyboards.inline import confirm_kb
from bot.template_engine import template_engine
from bot.states import Form
from bot.middlewares.resourses_middleware import ResourcesMiddleware

from sqlalchemy.ext.asyncio import AsyncSession


form_router = Router()
form_router.message.middleware(ResourcesMiddleware())  # adding middleware for messages
form_router.callback_query.middleware(ResourcesMiddleware())  # adding middleware for callbacks

logger = logging.getLogger(__name__)


@form_router.message(Form.want_create_bot, F.text.casefold() == "yes")  # reacts only when state is Form.like_bots
@form_router.callback_query(F.data == "confirm")
async def create_bot(message: Message, state: FSMContext, db_session: AsyncSession):
    await state.set_state(Form.idea)

    await message.answer("Excellent! What is your bot idea and functions?", reply_markup=ReplyKeyboardRemove)


@form_router.message(Form.want_create_bot, F.text.casefold() == "no")  # reacts only when state is Form.like_bots
async def not_create_bot(message: Message, state: FSMContext, db_session: AsyncSession):
    await state.clear()

    await message.answer("Oh, it's ok. Have  a good day!\nIf you still want to continue push the inline button",
                         reply_markup=confirm_kb())


@form_router.message(Form.idea)
async def get_bot_idea(message: Message, state: FSMContext, db_session: AsyncSession):
    await state.set_state(Form.language)
    await state.update_data(bot_idea=message.text)  # saving bot idea

    await message.answer("Great idea, what main language are you going to use?", reply_markup=ReplyKeyboardRemove)


@form_router.message(Form.language)
async def get_bot_language(message: Message, state: FSMContext, db_session: AsyncSession):
    await state.clear()
    data = await state.get_data()  # get saved data

    if message.text.lower() == "python":
        return await message.answer("What a coincidence! I have been developed with Python using aiogram.\n"
                                    f"I believe your bot with idea <{data['bot_idea']}> will be successful!",
                                    reply_markup=ReplyKeyboardRemove)

    await message.answer(f"I believe your bot on {message.text.lower()} with idea <{data['bot_idea']}> will be successful!",
                         reply_markup=ReplyKeyboardRemove)