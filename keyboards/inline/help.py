from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import _


def get_help_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(_('Цена'), switch_inline_query_current_chat=''))
    markup.add(InlineKeyboardButton(_('Конвертировать'), switch_inline_query_current_chat='2 ETH USD,EUR'))

    return markup
