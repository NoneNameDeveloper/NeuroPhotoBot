from loader import dp, _

from aiogram import types

from utils.db_api.models import User

from keyboards.inline import menu


@dp.message_handler(chat_type="private", commands=['start'])
async def start_private_handler(message: types.Message):

    msg = _("""
<b>👋 Hello!</b>

🔆 <b>Send a picture here, and I'll transform it into an anime style using a neural network.</b>

🐰 <i>You can also add a bot to the chat and have fun with friends!</i>
""")

    bot_me = await dp.bot.get_me()
    bot_username = bot_me.username

    await message.answer(msg, reply_markup=menu.add_to_chat(bot_username))
