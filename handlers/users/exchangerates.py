from aiogram.types import Message, InlineQuery, InputTextMessageContent, InlineQueryResultArticle

from loader import dp, bot
from utils import clean_html, get_price
from utils import generate_inline_id
from utils.misc import rate_limit


@dp.message_handler(exchange_rates=True)
@rate_limit(.5, 'exchange_rates')
async def exchange_rates(message: Message, amount, from_coins, to_coins):
    compare = get_price(from_coins, to_coins)

    await message.answer(get_text(compare, amount))


@dp.inline_handler(exchange_rates=True)
async def inline_exchange_rates(inline_query: InlineQuery, amount, from_coins, to_coins):
    compare = get_price(from_coins, to_coins)
    text = get_text(compare, amount)

    input_content = InputTextMessageContent(text)

    item = InlineQueryResultArticle(
        id=generate_inline_id(inline_query.query),
        title='Cryptocurrency',
        description=clean_html(text),
        thumb_url='https://is5-ssl.mzstatic.com/image/thumb/Purple128/v4/2e/d9/ed/2ed9ed62-fa5d-0ce7-8959'
                  '-e84b11ac049c/source/512x512bb.jpg',
        input_message_content=input_content,
    )

    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)


def get_text(compare: dict, amount: [int, float] = 1):
    if not compare:
        return 'Не найдено'

    text = ''
    for from_coin, to_coins_dict in compare.items():

        for key, value in to_coins_dict.items():
            text += f'<pre>{amount} {from_coin} = <b>{round(value * amount, 12)}</b> {key}</pre>\n'

        text += '\n'

    return text
