from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


def categories_keyboard():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Детское блюда"),
                KeyboardButton(text="Первые блюда")
            ],
            [
                KeyboardButton(text="Салаты"),
            ]
        ],
        resize_keyboard=True
    )
    return kb
#
# def review_rating_keyboard():
#     kb = ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text="Отлично")
#             ],
#             [
#                 KeyboardButton(text="Хорошо")
#             ],
#         ],
#         resize_keyboard=True
#     )
#     return kb