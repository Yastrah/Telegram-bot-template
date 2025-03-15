from aiogram.fsm.state import State, StatesGroup


# the name of a specific state corresponds to the expected response in that state
class Form(StatesGroup):
    want_create_bot = State()
    idea = State()
    language = State()
