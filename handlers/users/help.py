from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import Message, InlineQuery, InputTextMessageContent, InlineQueryResultArticle

from keyboards.inline import get_help_inline_markup
from loader import dp, bot, _
from utils import generate_inline_id


@dp.message_handler(CommandHelp())
async def bot_help(message: Message):
    text = get_text()

    await message.answer(text, reply_markup=get_help_inline_markup())


@dp.inline_handler()
async def inline_exchange_rates(inline_query: InlineQuery):
    text = get_text()

    input_content = InputTextMessageContent(text)

    item = InlineQueryResultArticle(
        id=generate_inline_id(inline_query.query),
        title=_('🆘 Помощь 🆘'),
        description='@cryptocompare_bot BTC\n@cryptocompare_bot 2 BTC USD,EUR',
        thumb_url='https://img.icons8.com/emoji/452/sos-button-emoji.png',
        input_message_content=input_content,
    )

    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)


def get_text():
    text = _('''
<b>🆘 Помощь 🆘</b>

<b>🔄 Конвертация 🔄</b>
<pre>@cryptocompare_bot [количество] {монета}/{монета}</pre>
<pre>@cryptocompare_bot BTC USD</pre>
<pre>@cryptocompare_bot 2 Btc usd</pre>
<pre>@cryptocompare_bot 4.55 BTC,ETH,DOGE / USD,EUR,RUB</pre>

<i>*Монеты для конвертации можно разделять через / либо через пробел, регистр монет не учитывается</i>

<b>💰 Цена 💰</b>
<pre>@cryptocompare_bot [количество] {монета}</pre>
<pre>@cryptocompare_bot BTC</pre>
<pre>@cryptocompare_bot 4 BTC</pre>
<pre>@cryptocompare_bot BTC,ETH,USD</pre>


<b>☎ Контакты ☎</b>
@briler
    ''')

    return text
