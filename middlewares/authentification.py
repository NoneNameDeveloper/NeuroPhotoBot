from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from aiogram.utils.markdown import quote_html
from aiogram import types

from utils.db_api.models import User, Chat
from utils.misc.language import language_message
from utils.misc.logger import logger_start, logger_group_start

from loader import dp

from data import config


class AuthentificationMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: types.Message, data: dict):

        if not message.chat.type == "private":
            return

        user_id = message.chat.id

        login = message.from_user.username

        # user registration to database
        user_check = User.select().where(User.user_id == user_id)
        if not user_check.exists():
            User.create(
                user_id=user_id,
                login=login
            )

            await dp.bot.send_message(
                chat_id=config.logs_chat,
                text=logger_start.format(
                    message.from_user.id,
                    message.from_user.username,
                    quote_html(message.from_user.full_name),
                    message.from_user.language_code
                ))

        user = User.get(User.user_id == message.chat.id)

        if user.language is None or user.language == "":

            await language_message(message)
            raise CancelHandler()

