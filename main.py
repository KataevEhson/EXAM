from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from dotenv import load_dotenv
from conection import *
from kayboards import *
from service import *
import os
import asyncio

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(token=BOT_TOKEN)


dp = Dispatcher()




@dp.message(F.text == "start")
@dp.message(Command("start"))
async def start_bot(message: Message):
    if await  get_user_by_id(message.from_user.id):
        status = await check_admin(message.from_user.id)
        if status:
                await message.answer("""
    🍔 Добро пожаловать Администратор!
    Здесь можно посмотреть меню, добавить блюда в корзину
    и изменить количество порций
    📋 Команды:
    /menu — посмотреть меню
    /dish ID — посмотреть блюдо, например /dish 1
    /cart — открыть свою корзину
    /clear_cart — очистить корзину
    /add_dish — добавить новое блюдо
    /cancel — отменить добавление блюда
    /help — помощь
    👇 Начни с /menu
""", reply_markup=admin_key)
        else:
            await message.answer("""
            🍔 Добро пожаловать в Food Order Bot!
            Здесь можно посмотреть меню, добавить блюда в корзину
            и изменить количество порций
            📋 Команды:
            /menu — посмотреть меню
            /dish ID — посмотреть блюдо, например /dish 1
            /cart — открыть свою корзину
            /clear_cart — очистить корзину
            /add_dish — добавить новое блюдо
            /cancel — отменить добавление блюда
            /help — помощь
            👇 Начни с /menu
        """, reply_markup=users_key)
    else:
        user = message.from_user
        await create_user(user.username, user.full_name, user.id)
        await message.answer(f"Привет @{message.from_user.username}", reply_markup=users_key)





@dp.message(F.text == "help")
@dp.message(Command("help"))
async def help_user_main(message : Message):
    await message.answer("""
Вот нашы команды и то что они делают
    /menu — посмотреть меню
    /dish ID — посмотреть блюдо, например /dish 1
    /cart — открыть свою корзину
    /clear_cart — очистить корзину
    /add_dish — добавить новое блюдо
    /cancel — отменить добавление блюда
    /help — помощь
""")





async def main():
    await create_table()
    print("Bot started")
    await dp.start_polling(bot)
    
    
    
if __name__ == "__main__":
    asyncio.run(main())