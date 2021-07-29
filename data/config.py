import os

from decouple import config as env_conf

DIR = os.path.dirname(os.path.realpath(__file__))

BOT_TOKEN = env_conf("BOT_TOKEN")
ADMINS = list(map(int, env_conf("ADMINS").split(',')))

DB_USER = env_conf('DATABASE_USER')
DB_PASSWORD = env_conf('DATABASE_PASS')
DB_HOST = env_conf('DATABASE_HOST')
DB_PORT = env_conf('DATABASE_PORT')

DB_NAME = env_conf('DATABASE_NAME', default='database.sqlite3', cast=str)

SQLALCHEMY_DATABASE_URI = f'sqlite+aiosqlite:///{DIR}/{DB_NAME}'

if DB_USER and DB_PASSWORD:
    SQLALCHEMY_DATABASE_URI = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

I18N_DOMAIN = 'bot'
LOCALES_DIR = f'{DIR}/locales'
