from aiogram import F, Router, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_review_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


ratings = ["Плохо", "Удовлетворительно", "Хорошо", "Отлично"]
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Плохо"), KeyboardButton(text="Удовлетворительно")],
        [KeyboardButton(text="Хорошо"), KeyboardButton(text="Отлично")]
    ]
)


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
    await state.update_data(phone_number=message.text)
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Дата вашего посещения (только цифры):")


@start_review_router.message(RestourantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(visit_date=message.text)
        await state.set_state(RestourantReview.food_rating)
        await message.answer("Как оцениваете качество еды?", reply_markup=keyboard)
    else:
        await message.answer("Пожалуйста, введите только цифры.")


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
        await message.answer("Пожалуйста, выберите одну из предложенных оценок.",reply_markup=keyboard)


@start_review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    user_data = await state.get_data()
    await message.answer("Спасибо за ваш отзыв!")
    await state.finish()