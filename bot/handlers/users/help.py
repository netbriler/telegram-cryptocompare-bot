from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import Message, InlineQuery, InputTextMessageContent, InlineQueryResultArticle

from bot.commands import get_default_commands, get_admin_commands
from bot.keyboards.inline import get_help_inline_markup
from loader import dp, bot, _
from models import User
from utils import generate_inline_id


@dp.message_handler(i18n_text='Help 🆘')
@dp.message_handler(CommandHelp())
async def _bot_help(message: Message, user: User):
    text = _get_text(user)

    await message.answer(text, reply_markup=get_help_inline_markup())


@dp.inline_handler()
async def _inline_exchange_rates(inline_query: InlineQuery, user: User):
    text = _get_text(user, inline=True)

    input_content = InputTextMessageContent(text)

    item = InlineQueryResultArticle(
        id=generate_inline_id(inline_query.query),
        title=_('Help 🆘'),
        description='@cryptocompare_bot BTC\n@cryptocompare_bot 2 BTC USD,EUR',
        thumb_url='https://img.icons8.com/emoji/452/sos-button-emoji.png',
        input_message_content=input_content,
    )

    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)


def _get_text(user: User, inline: bool = False):
    commands_text = ''
    if not inline:
        commands_text = _('<b>Commands 📝</b>\n')
        commands = get_admin_commands(user.language) if user.is_admin else get_default_commands(user.language)
        for command in commands:
            commands_text += f'{command.command} - {command.description}\n'
        commands_text += '\n'

    text = _('<b>Help 🆘</b>\n\n'

             '{commands}'

             '<b>Price 💰</b>\n'
             '<code>@cryptocompare_bot [quantity] coin</code>\n'
             '<code>@cryptocompare_bot BTC</code>\n'
             '<code>@cryptocompare_bot 4 BTC</code>\n'
             '<code>@cryptocompare_bot BTC,ETH,USD</code>\n\n'

             '<b>Conversion 🔄</b>\n'
             '<code>@cryptocompare_bot [quantity] coin / coin</code>\n'
             '<code>@cryptocompare_bot BTC USD</code>\n'
             '<code>@cryptocompare_bot 2 Btc usd</code>\n'
             '<code>@cryptocompare_bot 4.55 BTC,ETH,DOGE / USD,EUR,UAH</code>\n\n'

             '<i>*coins for conversion can be separated by / or by a space, the case of coins is insensitive </i>\n\n'

             '<b>Contact ☎</b>\n'
             '@briler').format(commands=commands_text)

    return text
