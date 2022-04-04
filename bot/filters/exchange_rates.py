import re

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, InlineQuery


class ExchangeRates(BoundFilter):
    key = 'exchange_rates'

    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    async def check(self, message, *args):
        if isinstance(message, Message):
            text = message.text.upper()
        elif isinstance(message, InlineQuery):
            text = message.query.upper()
        else:
            return False

        match = re.match('^((\d+([.|,]\d+)?)[/|\s]+)?([a-zA-Z|,]+)([/|\s]+([a-zA-Z|,]+))?$', text)
        if not match:
            return False

        if match.group(3):
            amount = float(match.group(2).replace(',', '.'))
        elif match.group(2):
            amount = int(match.group(2))
        else:
            amount = 1

        from_coins = match.group(4).split(',')

        if match.group(6):
            to_coins = match.group(6).split(',')
        else:
            to_coins = ['USD', 'EUR', 'UAH']

        if match:
            return {'amount': amount, 'from_coins': from_coins, 'to_coins': to_coins}
