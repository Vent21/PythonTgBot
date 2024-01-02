from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = [
    [
        KeyboardButton(text="☀️Погода"),
        KeyboardButton(text="🌆Рисунок"),
        # KeyboardButton(text="Button1_3")
    ],
    [
        KeyboardButton(text="🤖Вопрос ИИ"),
        KeyboardButton(text="📈Курс валют"),
        KeyboardButton(text="🎂Ближайшее ДР")
    ]
]
main_kb = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)

keyboard_for_kandinsky = [
    [
        KeyboardButton(text="Кандинский"),
        KeyboardButton(text="Ultra HD"),
    ],
    [
        KeyboardButton(text="Аниме"),
        KeyboardButton(text="Стандартный")
    ]
]

kandinsky_kb = ReplyKeyboardMarkup(
    keyboard=keyboard_for_kandinsky,
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)
