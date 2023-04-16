from aiogram import executor
from loader import dp
from db import init_db
import handlers


async def start_bot(dp):
    await init_db()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=start_bot, skip_updates=True)
