import asyncio
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()
token = getenv("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()


recipes = [
    "Рецепт 1: Овсянка с фруктами\n\nИнгредиенты:\n- Овсянка\n- Яблоко\n- Банан\n\nПриготовление:\n1. Сварите овсянку.\n2. Нарежьте фрукты.\n3. Смешайте и наслаждайтесь.",
    "Рецепт 2: Салат Цезарь\n\nИнгредиенты:\n- Куринная грудка\n- Салат Романо\n- Помидоры черри\n\nПриготовление:\n1. Обжарьте курицу.\n2. Нарежьте овощи.\n3. Смешайте с соусом и подавайте.",
    "Рецепт 3: Паста Карбонара\n\nИнгредиенты:\n- Спагетти\n- Бекон\n- Яйца\n\nПриготовление:\n1. Сварите спагетти.\n2. Обжарьте бекон.\n3. Смешайте с яйцами и подавайте.",
    "Рецепт 4: Борщ\n\nИнгредиенты:\n- Свекла\n- Капуста\n- Картофель\n\nПриготовление:\n1. Нарежьте овощи.\n2. Сварите в воде.\n3. Подайте с сметаной.",
    "Рецепт 5: Омлет\n\nИнгредиенты:\n- Яйца\n- Молоко\n- Сыр\n\nПриготовление:\n1. Взбейте яйца с молоком.\n2. Жарьте на сковороде.\n3. Посыпьте сыром и подавайте."
]


@dp.message(Command("start"))
async def start_command_handler(message: types.Message):
    await message.answer("Привет, "+message.from_user.first_name)


@dp.message(Command("myinfo"))
async def myinfo_command_handler(message: types.Message):
    info = (
            "Ваш id = " + str(message.from_user.id) + "\n" +
            "first_name = " + message.from_user.first_name + "\n" +
            "username = " + message.from_user.username
    )
    await message.answer(info)


@dp.message(Command("random_recipe"))
async def send_command_handler(message):
    recipe = random.choice(recipes)
    await message.answer(recipe)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())