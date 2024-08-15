from sqlite3 import DatabaseError

from aiogram import F, Router, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import re
from bot_config import database


start_review_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


ratings = ["1", "2", "3", "4","5"]
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1"), KeyboardButton(text="2")],
        [KeyboardButton(text="3"), KeyboardButton(text="4")],
        [KeyboardButton(text="5")]
    ]
)
DATE_PATTERN = re.compile(r'^\d{4}-\d{2}-\d{2}$')



@start_review_router.callback_query(F.data == 'feedback')
async def start_review(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await call.message.answer("Ваше имя?")


@start_review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.phone_number)
    await message.answer("Ваш номер телефона?")


@start_review_router.message(RestourantReview.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(phone_number=message.text)
        await state.set_state(RestourantReview.visit_date)
        await message.answer("Дата вашего посещения (YYYY-MM-dd):")
    else:
        await message.answer("Пожалуйста, введите в цифрах.")


@start_review_router.message(RestourantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    if DATE_PATTERN.match(message.text):
        await state.update_data(visit_date=message.text)
        await state.set_state(RestourantReview.food_rating)
        await message.answer("Как оцениваете качество еды?", reply_markup=keyboard)
    else:
        await message.answer("Пожалуйста, введите дату в формате YYYY-MM-DD.")


@start_review_router.message(RestourantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    if message.text in ratings:
        await state.update_data(food_rating=message.text)
        await state.set_state(RestourantReview.cleanliness_rating)
        await message.answer("Как оцениваете чистоту заведения?", reply_markup=keyboard)
    else:
        await message.answer("Пожалуйста, выберите одну из предложенных оценок.",reply_markup=keyboard)


@start_review_router.message(RestourantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    if message.text in ratings:
        await state.update_data(cleanliness_rating=message.text)
        await state.set_state(RestourantReview.extra_comments)
        await message.answer("Дополнительные комментарии:")
    else:
        await message.answer("Пожалуйста, выберите одну из предложенных оценок.")


@start_review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    user_data = await state.get_data()
    database.execute(
        query="INSERT INTO survey (name, phone_number, visit_date, food_rating, cleanliness_rating, extra_comments) VALUES (?, ?, ?, ?, ?, ?)",
        params=(
            user_data.get('name'),
            user_data.get('phone_number'),
            user_data.get('visit_date'),
            int(user_data.get('food_rating')),
            int(user_data.get('cleanliness_rating')),
            user_data.get('extra_comments')
        )
    )
    await message.answer("Спасибо за ваш отзыв!")
    await state.clear()