from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, InlineQuery

from loader import logger


class LoggingMiddleware(BaseMiddleware):
    """
    Simple logging
    """

    def __init__(self):
        super(LoggingMiddleware, self).__init__()

    @staticmethod
    async def on_process_message(message: Message, data: dict):
        if message.content_type == 'text':
            logger.debug(f'from_user: {message.from_user.id} message_id: {message.message_id} text: {message.text}')

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict):
        logger.debug(
            f'from_user: {inline_query.from_user.id} inline_query_id: {inline_query.id} query: {inline_query.query}')
