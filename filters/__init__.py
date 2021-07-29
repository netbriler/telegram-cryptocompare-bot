from aiogram import Dispatcher

from loader import dp
from .exchange_rates import ExchangeRates


if __name__ == 'filters':
    dp.filters_factory.bind(ExchangeRates)
