from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_help_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('Цена', switch_inline_query_current_chat='ETH'))
    markup.add(InlineKeyboardButton('Конвертировать', switch_inline_query_current_chat='2 ETH USD,EUR'))

    return markup
