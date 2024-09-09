import random
import time

from aiogram import Bot, Dispatcher, executor
from aiogram import types

API_TOKEN = '7067512062:AAEFPz-9GiSq4hl5b8dyNoCQrU3003sghck'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def get_texts_as_list():
    with open('texts.txt', 'r') as file:
        a = file.readlines()
        for i in range(len(a)):
            a[i] = a[i].strip()

    return a


@dp.message_handler(commands=['posvyatfes'])
async def example_func(message: types.Message):
    texts = get_texts_as_list()
    await message.answer(random.choice(texts))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
