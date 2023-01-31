from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

import logging


logging.basicConfig(level=logging.INFO)

bot = Bot(config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())


from middlewares.i18n import ACLMiddleware

i18n = ACLMiddleware(config.I18N_DOMAIN, config.LOCALES_DIR)
dp.middleware.setup(i18n)
_ = i18n.gettext


from middlewares.authentification import AuthentificationMiddleware

dp.middleware.setup(AuthentificationMiddleware())
