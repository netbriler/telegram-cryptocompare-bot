from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import _


def get_language_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.row(InlineKeyboardButton('🇺🇸 English', callback_data='lang_en'),
               InlineKeyboardButton('🇷🇺 Русский', callback_data='lang_ru'),
               InlineKeyboardButton('🇺🇦 Українська', callback_data='lang_uk'))

    return markup
