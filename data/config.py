from decouple import config as env_conf
import os

DIR = os.path.dirname(os.path.realpath(__file__))

BOT_TOKEN = env_conf("BOT_TOKEN")
ADMINS = list(map(int, env_conf("ADMINS").split(',')))

SQLALCHEMY_DATABASE_URI = f'sqlite+aiosqlite:///{DIR}/database.sqlite3'
