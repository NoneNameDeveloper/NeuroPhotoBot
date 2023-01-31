from loader import dp, _

from aiogram import types
from aiogram.utils.markdown import quote_html

from utils.db_api.models import Chat

from keyboards.inline import menu

from data import config

from utils.misc.logger import logger_group_start


@dp.message_handler(chat_type=["group", "supergroup"], commands=["start"])
async def welcome_group__handler(message: types.Message):

    new_lang = None

    chat_id = message.chat.id
    login = message.chat.username

    # user registration to database
    chat_check = Chat.select().where(Chat.chat_id == chat_id)

    if not chat_check.exists():
        new_lang = "ru"
        Chat.create(
            chat_id=chat_id,
            chat_name=login if login else "None",
            language=new_lang
        )

        await dp.bot.send_message(
            chat_id=config.logs_chat,
            text=logger_group_start.format(
                message.from_user.id,
                message.from_user.username,
                quote_html(message.from_user.full_name),
                message.chat.id,
                quote_html(message.chat.title),
                message.chat.username,
                await message.chat.get_member_count()
            ))

    if new_lang:
        return await message.answer(_("""
<b>👋 Hello!</b>

🔆 <b>Send a picture here, and I'll transform it into an anime style using a neural network.</b>

<i>🌐 /lang - change language</i>
""", locale=new_lang))

    chat = Chat.get(Chat.chat_id == message.chat.id)

    return await message.answer(_("""
<b>👋 Hello!</b>

🔆 <b>Send a picture here, and I'll transform it into an anime style using a neural network.</b>

<i>🌐 /lang - change language</i>
""", locale=chat.language))