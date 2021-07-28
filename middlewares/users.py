from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, InlineQuery

from services.users import get_or_create_user


class UsersMiddleware(BaseMiddleware):
    """
    Simple logging
    """

    @staticmethod
    async def on_process_message(message: Message, data: dict):
        session = data['session'] = message.bot.get('session')

        user = await get_or_create_user(session, id=message.from_user.id, name=message.from_user.full_name,
                                        username=message.from_user.username, language=message.from_user.language_code)

        data['user'] = user

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict):
        session = data['session'] = inline_query.bot.get('session')

        user = await get_or_create_user(session, id=inline_query.from_user.id, name=inline_query.from_user.full_name,
                                        username=inline_query.from_user.username,
                                        language=inline_query.from_user.language_code)

        data['user'] = user
