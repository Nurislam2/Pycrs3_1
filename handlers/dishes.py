from aiogram import Router, types, F


dishes_router = Router()


@dishes_router.message(F.text=="Холодные Напитки")
async def drinks_handler(message: types.Message):
    image=types.FSInputFile("pictures/cocacola.jpg")
    await message.answer_photo(photo=image,caption="Coca-Cola")


@dishes_router.message(F.text=="Завтраки")
async def breakfast_handler(message: types.Message):
    image=types.FSInputFile("pictures/breakfast.jpg")
    await message.answer_photo(photo=image,caption="Яичница с салатом")


@dishes_router.message(F.text=="Горячие блюда")
async def Hot_dishes_handler(message: types.Message):
    image=types.FSInputFile("pictures/dishes.jpg")
    await message.answer_photo(photo=image,caption="Жаркое")
