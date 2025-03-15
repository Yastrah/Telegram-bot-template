from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def yes_no_kb() -> ReplyKeyboardMarkup:
    """
    Keyboard with buttons Yes and No
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="Yes")
    kb.button(text="No")
    kb.adjust(2)
    # kb.adjust(3, 2)  # first line 3 buttons, in the second 2 buttons
    return kb.as_markup(resize_keyboard=True)  # resize to make buttons proportional


def main_menu_kb() -> ReplyKeyboardMarkup:
    """
    Keyboard for Main Menu
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="Greeting")
    kb.button(text="Info")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
