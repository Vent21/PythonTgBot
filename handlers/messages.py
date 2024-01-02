from currency import get_rates
from weather import get_weather
from birthday_reminder import get_birthday
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart


from keyboards import reply


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    print(message.text)
    await message.reply(text="Привет!", reply_markup=reply.main_kb)


@router.message(F.text.lower() == "📈курс валют")
async def send_currency(message: Message):
    print(message.text.lower())
    await message.reply(text=get_rates())


@router.message(F.text.lower() == "☀️погода")
async def send_weather(message: Message):
    await message.reply(text=get_weather())


@router.message(F.text.lower() == "🎂ближайшее др")
async def send_birthday(message: Message):
    await message.reply(text=get_birthday())
