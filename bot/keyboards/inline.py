from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def confirm_kb() -> InlineKeyboardMarkup:
    """
    Keyboard with one button to confirm
    """
    kb = InlineKeyboardBuilder()
    kb.button(text="✅", callback_data="confirm")  # ✅❌
    return kb.as_markup()
