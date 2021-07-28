"""

pybabel extract --input-dirs=. -o data/locales/bot.pot --project=bot

pybabel init -i data/locales/bot.pot -d locales -D bot -l en
pybabel init -i data/locales/bot.pot -d locales -D bot -l ru
pybabel init -i data/locales/bot.pot -d locales -D bot -l uk

pybabel compile -d locales -D bot
"""

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from data.config import I18N_DOMAIN, LOCALES_DIR
from services.users import get_user


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action, args):
        current_telegram_user = types.User.get_current()

        user = await get_user(args[0].bot.get('session'), current_telegram_user.id)

        if user:
            return user.language

        return current_telegram_user.locale


i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
