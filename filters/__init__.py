from aiogram import Dispatcher

from loader import dp
from .is_super_admin import SuperAdminFilter
from .exchange_rates import ExchangeRates


if __name__ == "filters":
    dp.filters_factory.bind(SuperAdminFilter)
    dp.filters_factory.bind(ExchangeRates)
