from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from service import *
from kayboards import *
from aiogram.types import CallbackQuery


router = Router()






@router.callback_query(F.data.startswith("dish:"))
async def details(callback: CallbackQuery):
    await callback.answer()
    dish_id = int(callback.data.split(":")[1])
    dish = await get_dish_by_id(dish_id)
    if not dish:
        return await callback.message.answer("Такого блюдо нету😭")
    await callback.message.answer_photo(
        photo=dish["photo_file_id"],
        caption=f"""
Title: {dish['title']}
Description:  {dish['description']}
Цена: {dish['price']}"""
)

















