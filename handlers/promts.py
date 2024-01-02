import base64
import os

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import gpt
import kandinsky
from data.configs import KANDINSKY_API_KEY, KANDINSKY_SECRET_KEY
from keyboards.reply import kandinsky_kb, main_kb
from states.states import Promt, AIAsk

# from gpt import ask_gpt
# from giga_chat import get_gigachat_response

router = Router()


@router.message(F.text.lower() == "🌆рисунок")
async def get_promt(message: Message, state: FSMContext):
    await message.answer(text="Введите промт")
    await state.set_state(Promt.promt)


@router.message(Promt.promt)
async def get_style(message: Message, state: FSMContext):
    await state.update_data(promt=message.text)
    await state.set_state(Promt.style)
    await message.reply(text="Выберите стиль", reply_markup=kandinsky_kb)


@router.message(Promt.style)
async def send_picture(message: Message, state: FSMContext):
    # await state.update_data(promt=message.text)
    styles = ["Кандинский", "Ultra HD", "Аниме", "Стандартный"]
    style_string = message.text

    if style_string in styles:
        style = styles.index(style_string)
    else:
        style = 3

    await message.reply(text=f"Выбран стиль: {message.text}\nОжидайте, обработка запроса займет около 30 секунд",
                        reply_markup=main_kb)
    data = await state.get_data()
    await state.clear()
    print(data.get("promt"))
    api = kandinsky.Text2Image("https://api-key.fusionbrain.ai/", KANDINSKY_API_KEY, KANDINSKY_SECRET_KEY)
    model_id = api.get_model()
    uuid = api.generate(data.get("promt"), model_id, style)
    images = api.check_generation(uuid)

    image_base64 = images[0]

    image_data = base64.b64decode(image_base64)

    try:
        with open("data/image.jpg", "wb") as file:
            file.write(image_data)
    except FileNotFoundError:
        with open("data/image.jpg", "w+") as file:
            # file.write(image_data)
            await message.answer("Что то пошло не так")
            file.close()

    path = "data/image.jpg"

    if os.path.exists(path):
        await message.answer_photo(photo=types.FSInputFile(path=path))
    else:
        await message.answer("Сервис временно недоступен")


@router.message(F.text.lower() == "🤖вопрос ии")
async def get_ai_response(message: Message, state: FSMContext):
    await message.answer(text="Спрашивай")
    await state.set_state(AIAsk.ask)


@router.message(AIAsk.ask)
async def send_ai_response(message: Message, state: FSMContext):
    await message.answer("Хмм... 🤔 Дай подумать")
    print(message.text)
    # string = await message.reply(text=get_gigachat_response(message.text))
    string = await gpt.ask_gpt(message.text)
    await message.reply(text=string)
    # await message.reply(text=get_gigachat_response(message.text))
    await state.clear()
