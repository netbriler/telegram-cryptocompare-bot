from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message

from bot.keyboards.inline import get_language_inline_markup
from loader import dp, _


@dp.message_handler(CommandStart())
async def _bot_start(message: Message):
    text = _('Hi {full_name}!\n'
             'Choose your language').format(full_name=message.from_user.full_name)

    await message.answer(text, reply_markup=get_language_inline_markup())
