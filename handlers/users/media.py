from aiogram import types

from keyboards.inline import menu
from loader import dp, _

from io import BytesIO

from engine import AnimeProcess


@dp.message_handler(chat_type="private", content_types=["photo"])
async def photo_private_process_handler(message: types.Message):

    msg_to_delete = await message.answer(_("""
🌠 Photo processing..
Wait ~10 seconds    
"""))

    photo_id = message.photo[-1].file_id
    image_obj = await dp.bot.get_file(photo_id)

    with BytesIO() as container_data:
        await image_obj.download(destination_file=container_data)

        anime_model = await AnimeProcess.get_anime_data(container_data.read())

    # service returned an error
    if anime_model.code != 0:
        error_msg = _("""
⛔️<b> Service have returned an error.</b>

<b>✒️ Error body:</b> <i>{}</i>   
""")
        return await msg_to_delete.edit_text(
            text=error_msg.format(anime_model.msg),
            reply_markup=menu.to_close()
        )

    await msg_to_delete.delete()

    await message.reply_photo(anime_model.extra[0])
    