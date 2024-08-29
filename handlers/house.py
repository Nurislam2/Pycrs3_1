from aiogram import Router, types
from aiogram.filters.command import Command
from crawler.house_kg import HouseCrawler

house_router = Router()


@house_router.message(Command("house"))
async def show_house_handler(message: types.Message):
    crawler = HouseCrawler()
    crawler.get_page()
    links = crawler.get_house_link()
    photos = crawler.get_house_photo()
    details = crawler.get_house_details()
    addresses = crawler.get_house_address()
    for i in range(len(links)):
        caption = f"{details[i]}\n{addresses[i]}\n{links[i]}"
        await message.answer_photo(photo=photos[i], caption=caption)
