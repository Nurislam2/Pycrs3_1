from aiogram import Router,types
from aiogram.filters.command import Command


myInfo_router = Router()


@myInfo_router.message(Command("myinfo"))
async def myinfo_command_handler(message: types.Message):
    info = (
            "Ваш id = " + str(message.from_user.id) + "\n" +
            "first_name = " + message.from_user.first_name + "\n" +
            "username = " + message.from_user.username
    )
    await message.answer(info)

