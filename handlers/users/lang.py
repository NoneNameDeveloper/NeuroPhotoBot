from loader import dp, _

from aiogram import types

from keyboards.inline import menu


@dp.message_handler(commands=['lang'], chat_type=['private', "group", "supergroup"])
async def private_start_handler(message: types.Message):

    msg = _("🌐 <b>Choose new language</b>")

    await message.answer(msg, reply_markup=menu.language_markup())
