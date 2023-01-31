from data.config import ADMINS


async def on_startup_notify(dp):
    """
    notify about bot has been started to admins
    :param dp:
    :type dp:
    :return:
    :rtype:
    """
    for u in ADMINS:
        if u:
            await dp.bot.send_message(u, "⚡️ Bot was started")