import os
import asyncio
import logging
from aiogram import Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram import Bot

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Assalomu Aleykum, Xurmatli {message.from_user.mention_html()}")


async def main() -> None:
    bot = Bot(token=os.environ.get('TOKEN'), parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "main":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
