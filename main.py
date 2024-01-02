import asyncio
import logging


from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

# from aiogram.dispatcher.filters import Text


async def get_start(message: types.Message, bot: Bot):
    await message.answer(f"Привет {message.from_user.first_name}!")
