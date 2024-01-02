import asyncio
import logging

from aiogram import Bot, Dispatcher
from data.configs import BOT_TOKEN
from handlers import messages, promts


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(messages.router, promts.router)
    # dp.message.register(messages.start)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
