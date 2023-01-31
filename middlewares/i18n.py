from typing import Tuple, Any

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from utils.db_api.models import User


async def get_lang(user_id: int) -> str:
    """
    getting user's locale from database
    :param user_id: telegram user_id
    :type user_id: int
    :return: user locale
    :rtype: str
    """
    try:
        user = User.get(User.user_id == user_id)

        return user.language
    except Exception as e:
        return False


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]):
        user = types.User.get_current()
        return await get_lang(user.id) or user.locale
