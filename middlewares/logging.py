from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, InlineQuery

from utils.misc.logging import logger


class LoggingMiddleware(BaseMiddleware):
    """
    Simple logging
    """

    def __init__(self):
        super(LoggingMiddleware, self).__init__()

    @staticmethod
    async def on_process_message(message: Message, data: dict):
        if message.content_type == 'text':
            logger.debug(f'Received message [ID:{message.message_id}] from user [{message.from_user.id}] '
                         f'text "{message.text}"')

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict):
        logger.debug(f'Received inline query [query:{inline_query.query}] from user [ID:{inline_query.from_user.id}]')
