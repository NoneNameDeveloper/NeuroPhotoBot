from loader import dp, _

from aiogram import types

from utils.db_api.models import Chat
from keyboards.inline import menu


# SET NEW LANGUAGE
@dp.callback_query_handler(chat_type=["group", "supergroup"], text_contains="setlang_")
async def new_lang_set_handler(call: types.CallbackQuery):

    await call.answer()

    user_id = call.message.chat.id

    new_lang = call.data.split('_')[1]

    chat = Chat.get(Chat.chat_id == user_id)
    chat.language = new_lang
    chat.save()

    await call.message.edit_text(_("✅ New language successfully set!", locale=new_lang))

    msg = _("""
<b>👋 Hello!</b>

🔆 <b>Send a picture here, and I'll transform it into an anime style using a neural network.</b>

<i>🌐 /lang - change language</i>
    """, locale=new_lang)

    bot_me = await dp.bot.get_me()
    bot_username = bot_me.username

    await call.message.answer(msg, reply_markup=menu.add_to_chat(bot_username))
