import os

from decouple import config as env_conf

DIR = os.path.dirname(os.path.realpath(__file__))

BOT_TOKEN = env_conf("BOT_TOKEN")
ADMINS = list(map(int, env_conf("ADMINS").split(',')))

DB_USER = env_conf('DATABASE_USER', default=None)
DB_PASSWORD = env_conf('DATABASE_PASS', default=None)
DB_HOST = env_conf('DATABASE_HOST', default=None)
DB_PORT = env_conf('DATABASE_PORT', default=None)
DB_NAME = env_conf('DATABASE_NAME', default=None)

SQLALCHEMY_DATABASE_URI = f'sqlite+aiosqlite:///{DIR}/database.sqlite3'

if DB_USER and DB_PASSWORD and DATABASE_HOST and DB_PORT and DB_NAME:
    SQLALCHEMY_DATABASE_URI = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

I18N_DOMAIN = 'bot'
LOCALES_DIR = f'{DIR}/locales'
