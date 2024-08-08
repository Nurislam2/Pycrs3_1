import asyncio
import logging

from handlers.start import start_router
from handlers.myInfo import myInfo_router
from handlers.random_recipe import random_recipe_router
from handlers.dishes import dishes_router
from bot_config import bot, dp


async def main():
    dp.include_router(start_router)
    dp.include_router(myInfo_router)
    dp.include_router(random_recipe_router)
    dp.include_router(dishes_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())