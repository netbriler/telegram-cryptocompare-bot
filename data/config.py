from decouple import config as env_conf

BOT_TOKEN = env_conf("BOT_TOKEN")
ADMINS = list(map(int, env_conf("ADMINS").split(',')))
