from loader import dp
from .admin import Admin
from .exchange_rates import ExchangeRates
from .i18n_text import I18nText

if __name__ == 'bot.filters':
    dp.filters_factory.bind(Admin)
    dp.filters_factory.bind(I18nText)
    dp.filters_factory.bind(ExchangeRates)
