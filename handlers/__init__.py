from aiogram import F, Router

from .dishes import dishes_router
from .myInfo import myInfo_router
from .random_recipe import random_recipe_router
from .start import start_router
from .review_dialog import start_review_router
from .group import group_router
from .house import house_router

private_router = Router()

private_router.include_router(start_router)
private_router.include_router(myInfo_router)
private_router.include_router(random_recipe_router)
private_router.include_router(start_review_router)
private_router.include_router(house_router)


private_router.message.filter(F.chat.type == "private")