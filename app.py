from aiogram import executor

import middlewares
import filters
import handlers

from loader import dp, logger


async def on_startup(dispatcher):
    logger.info('Bot startup')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
