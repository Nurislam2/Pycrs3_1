import random
from aiogram import Router,types
from aiogram.filters.command import Command


random_recipe_router = Router()


recipes = [
    "Рецепт 1: Овсянка с фруктами\n\nИнгредиенты:\n- Овсянка\n- Яблоко\n- Банан\n\nПриготовление:\n1. Сварите овсянку.\n2. Нарежьте фрукты.\n3. Смешайте и наслаждайтесь.",
    "Рецепт 2: Салат Цезарь\n\nИнгредиенты:\n- Куринная грудка\n- Салат Романо\n- Помидоры черри\n\nПриготовление:\n1. Обжарьте курицу.\n2. Нарежьте овощи.\n3. Смешайте с соусом и подавайте.",
    "Рецепт 3: Паста Карбонара\n\nИнгредиенты:\n- Спагетти\n- Бекон\n- Яйца\n\nПриготовление:\n1. Сварите спагетти.\n2. Обжарьте бекон.\n3. Смешайте с яйцами и подавайте.",
    "Рецепт 4: Борщ\n\nИнгредиенты:\n- Свекла\n- Капуста\n- Картофель\n\nПриготовление:\n1. Нарежьте овощи.\n2. Сварите в воде.\n3. Подайте с сметаной.",
    "Рецепт 5: Омлет\n\nИнгредиенты:\n- Яйца\n- Молоко\n- Сыр\n\nПриготовление:\n1. Взбейте яйца с молоком.\n2. Жарьте на сковороде.\n3. Посыпьте сыром и подавайте."
]


@random_recipe_router.message(Command("random_recipe"))
async def send_command_handler(message):
    recipe = random.choice(recipes)
    await message.answer(recipe)
