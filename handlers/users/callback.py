from loader import dp, _

from aiogram import types

from utils.db_api.models import User
from keyboards.inline import menu


# SET NEW LANGUAGE
@dp.callback_query_handler(chat_type=["private"], text_contains="setlang_")
async def new_lang_set_handler(call: types.CallbackQuery):

    user_id = call.from_user.id

    new_lang = call.data.split('_')[1]

    user = User.get(User.user_id == user_id)
    user.language = new_lang
    user.save()

    await call.message.edit_text(_("✅ New language successfully set!", locale=new_lang))

    msg = _("""
<b>👋 Hello!</b>

🔆 <b>Send a picture here, and I'll transform it into an anime style using a neural network.</b>

🐰 <i>You can also add a bot to the chat and have fun with friends!</i>
""", locale=new_lang)

    bot_me = await dp.bot.get_me()
    bot_username = bot_me.username

    await call.message.answer(msg, reply_markup=menu.add_to_chat(bot_username))


@dp.callback_query_handler(text="to_close")
async def to_close_message_handler(call: types.CallbackQuery):

    await call.message.delete()
