from dotenv import load_dotenv
import os

load_dotenv("env.env")

BOT_TOKEN = os.getenv('BOT_TOKEN')

ADMINS = os.getenv('ADMINS').split(',')

POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

I18N_DOMAIN = os.getenv('I18N_DOMAIN')
LOCALES_DIR = os.getenv('LOCALES_DIR')

logs_chat = os.getenv("LOGS_CHAT")