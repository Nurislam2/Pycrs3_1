from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from handlers.review_dialog import RestourantReview

start_router = Router()


@start_router.message(Command("start"))
async def start_command_handler(message: types.Message):
    kb=types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш адрес",url="https://2gis.kg/bishkek/geo/15763234351127723/74.58716%2C42.884312?m=74.587282%2C42.884402%2F19.97"),
                types.InlineKeyboardButton(text="Контакты", callback_data="Контакты"),
            ],
            [
                types.InlineKeyboardButton(text="Наши вакансии", callback_data="Вакансии"),
                types.InlineKeyboardButton(text="Оставить Отзыв", callback_data="feedback")
            ],
            [
                types.InlineKeyboardButton(text="Блюда",callback_data="dishes")
            ]
        ])
    await message.answer("Здраствуйте! Добро подаловать в Кафе Фаиза",reply_markup=kb)


@start_router.callback_query(F.data=="Контакты")
async def contact_handler(callback: types.CallbackQuery):
    await callback.message.answer("Администратор:0555884466"+"\n"+
                                  "Для заказа:0226448877")


@start_router.callback_query(F.data=="Вакансии")
async def vacancies_handler(callback: types.CallbackQuery):
    await callback.message.answer("Требуется официант 1,90"+"\n"+
                                  "Требуется повар со знанием Кулинарии")


@start_router.callback_query(F.data == 'feedback')
async def start_review(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await call.message.answer("Ваше имя?")

