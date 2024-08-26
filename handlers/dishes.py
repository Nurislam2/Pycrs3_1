import sqlite3

from aiogram import Router, types, F
from aiogram.filters.command import Command

from keyboards import categories_keyboard
from bot_config import database


dishes_router = Router()


@dishes_router.message(Command("dishes"))
async def shop_command_handler(message: types.Message):
    await message.answer("Выберите категорию блюд", reply_markup=categories_keyboard())


categories = {"Детское блюда", "Первые блюда", "Салаты"}


@dishes_router.message(F.text.lower())
async def genres_handler(message: types.Message):
    category = message.text
    kb = types.ReplyKeyboardRemove()

    dishes = database.fetch(
        """
            SELECT * FROM dishes 
            JOIN categories ON dishes.category_id = categories.id 
            WHERE categories.name = ?
        """,
        (category.capitalize(),)
    )
    if not dishes:
        await message.answer(f"Блюда по категории {category} нет ")
        return

    # pprint(books)
    await message.answer(
        f"Блюда по категории {category}: ",
        reply_markup=kb
    )
    for dish in dishes:
        image=types.FSInputFile(dish[3])
        await message.answer_photo(photo=image, caption=f"Название: {dish[1]}\nЦена: {dish[2]} сом")
