from aiogram import executor
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards import *
from config import dp
from texts import *


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Команды
@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(on_start_text, reply_markup=main_kb)


# Расчет калорий
@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=inline_calculate_kb)

@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer(formulas_text)
    await call.answer()

@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст.")
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост.")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес.")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(formula_result(data))
    await state.finish()


# Покупка
@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for i in range(4):
        with open(product_info_img[i], "rb") as img:
            await message.answer_photo(img, product_info_text[i])
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_buying_kb)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


# Неизвестная команда/сообщение
@dp.message_handler()
async def all_messages(message):
    await message.answer(all_messages_text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
