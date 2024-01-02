from aiogram.fsm.state import StatesGroup, State


class Promt(StatesGroup):
    promt = State()
    style = State()


class AIAsk(StatesGroup):
    ask = State()
