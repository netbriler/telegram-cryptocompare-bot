from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = f'''
Привет, {message.from_user.full_name}!
Нажми /help чтобы узнать чем я могу тебе помочь
    '''

    await message.answer(text)