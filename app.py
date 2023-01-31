from loader import dp

from aiogram import executor

from utils import set_bot_commands, on_startup_notify

import handlers


async def on_startup(dp):

    await set_bot_commands(dp)

    await on_startup_notify(dp)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
