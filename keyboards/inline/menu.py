from aiogram import types
from loader import _

locales_dict = {
    "ru": "🇷🇺 Русский",
    "en": "🇬🇧 English"
}


def add_to_chat(username: str):
    markup = types.InlineKeyboardMarkup()

    markup.insert(
        types.InlineKeyboardButton(
            text=_("Add"), url=f"https://t.me/{username}?startgroup=true"
        )
    )

    return markup


def language_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)

    for lang in locales_dict.keys():
        markup.insert(
            types.InlineKeyboardButton(
                text=(locales_dict[lang]), callback_data=f"setlang_{lang}"
            )
        )

    return markup


def to_close():
    markup = types.InlineKeyboardMarkup()

    markup.insert(
        types.InlineKeyboardButton(
            text=_("Close"), callback_data="to_close"
        )
    )

    return markup
