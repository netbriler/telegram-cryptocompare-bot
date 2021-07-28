from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .logging import LoggingMiddleware
from .users import UsersMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(LoggingMiddleware())
    dp.middleware.setup(UsersMiddleware())
