from aiogram.fsm.state import State, StatesGroup


# the name of a specific state corresponds to the expected response in that state
# for example state 'name' by meaning is 'waiting_for_name'

class FormStates(StatesGroup):
    want_create_bot = State()
    get_idea = State()
    get_language = State()


class RegistrationStates(StatesGroup):
    get_name = State()
    get_password = State()
