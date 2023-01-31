from keyboards.inline import menu


async def language_message(message):

    msg = ("""
🇷🇺 Выберите язык

🇬🇧 Choose language
""")

    await message.answer(msg, reply_markup=menu.language_markup())
