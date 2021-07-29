from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, _

from keyboards.inline import get_language_inline_markup


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = _('Привет, {full_name}!\n'
             'Выбери свой язык').format(full_name=message.from_user.full_name)

    await message.answer(text, reply_markup=get_language_inline_markup())
