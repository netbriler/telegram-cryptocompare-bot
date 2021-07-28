from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, _


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = _('''
Привет, {full_name}!
Нажми /help чтобы узнать чем я могу тебе помочь
    ''').format(full_name=message.from_user.full_name)

    await message.answer(text)
