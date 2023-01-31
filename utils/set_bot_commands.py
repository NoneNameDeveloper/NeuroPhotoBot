from aiogram import types


async def set_bot_commands(dp):
    """
    setting commands to bot
    :param dp:
    :type dp:
    :return:
    :rtype:
    """
    bot_commands = [
        types.BotCommand("start", "start the bot"),
        types.BotCommand("lang", "change language")
    ]

    await dp.bot.set_my_commands(bot_commands)
