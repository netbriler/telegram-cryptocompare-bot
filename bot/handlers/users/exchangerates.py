from aiogram.types import Message, InlineQuery, InputTextMessageContent, InlineQueryResultArticle

from loader import dp, bot, _
from services.cryptocompare import get_price
from utils import clean_html
from utils import generate_inline_id
from utils.misc import rate_limit


@dp.message_handler(exchange_rates=True)
@rate_limit(.5, 'exchange_rates')
async def exchange_rates(message: Message, amount: [int, float], from_coins: str, to_coins: str):
    compare = get_price(from_coins, to_coins)

    await message.answer(_get_text(compare, amount))


@dp.inline_handler(exchange_rates=True)
async def inline_exchange_rates(inline_query: InlineQuery, amount: [int, float], from_coins: str, to_coins: str):
    compare = get_price(from_coins, to_coins)
    text = _get_text(compare, amount)

    input_content = InputTextMessageContent(text)

    item = InlineQueryResultArticle(id=generate_inline_id(inline_query.query), title='Cryptocurrency',
                                    description=clean_html(text), thumb_url='https://shorturl.at/dkrtD',
                                    input_message_content=input_content)

    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)


def _get_text(compare: dict, amount: [int, float] = 1) -> str:
    if not compare:
        return _('Not found')

    text = ''
    for from_coin, to_coins_dict in compare.items():

        for key, value in to_coins_dict.items():
            text += f'<code>{amount} {from_coin} = <b>{round(value * amount, 12)}</b> {key}</code>\n'

        text += '\n'

    return text
