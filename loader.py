import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.misc.logging import file_logger, client_logger

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
logger.addHandler(file_logger)
logger.addHandler(client_logger)

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
