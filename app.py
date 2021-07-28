from aiogram import executor

import middlewares
import filters
import handlers

from loader import dp, logger, bot

from utils.db.base import create_async_database


async def on_startup(dispatcher):
    logger.info('Bot startup')

    bot['session'] = await create_async_database()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
