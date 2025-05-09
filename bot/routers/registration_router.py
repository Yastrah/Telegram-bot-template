import logging

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from bot.services.registration_service import AuthService
from sqlalchemy.ext.asyncio import AsyncSession

from bot.states import RegistrationStates

registration_router = Router()
logger = logging.getLogger(__name__)


@registration_router.message(Command("register"))
@registration_router.message(F.text.casefold() == "register")
async def start_registration(message: types.Message, db_session: AsyncSession, state: FSMContext):
    auth = AuthService(db_session)

    if await auth.is_registered(message.from_user.id):
        await message.answer("✅ Вы уже зарегистрированы!")
        return

    # Запуск процесса регистрации через FSM
    await state.set_state(RegistrationStates.get_name)
    await message.answer("Введите ваше имя:")


@registration_router.message(RegistrationStates.get_name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text

    # name validation

    await state.update_data(name=name)
    await state.set_state(RegistrationStates.get_password)
    await message.answer("Введите пароль:")


@registration_router.message(RegistrationStates.get_password)
async def process_password(message: types.Message, db_session: AsyncSession, state: FSMContext):
    password = message.text

    # password validation

    data = await state.get_data()
    auth = AuthService(db_session)

    user = await auth.register_user(
        telegram_id=message.from_user.id,
        user_name=data['name'],
        password=password
    )
    await state.clear()
    if user:
        return await message.answer(
            f"🎉 Регистрация завершена, {data['name']}!\n\n"
            f"Ваш ID: {user.id}\n"
            f"Имя: {user.login}\n"
            f"Телефон: {user.password}"
        )

    await message.answer("Не удалось зарегистрировались!")

