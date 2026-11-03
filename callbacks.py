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
    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Добавить",callback_data=f"cart:{dish['id']}")],
        
        [InlineKeyboardButton(text="➕",callback_data=f"plus:{dish['id']}")],

        [InlineKeyboardButton(text="➖",callback_data=f"minus:{dish['id']}")],

        [InlineKeyboardButton(text="🗑 Удалить",callback_data=f"delete:{dish['id']}")],

        [InlineKeyboardButton(text="❌ Cancel", callback_data="cancel:")]
    ])
    await callback.message.answer_photo(
        photo=dish["photo_file_id"],
        caption=f"""
Title: {dish['title']}
Description:  {dish['description']}
Цена: {dish['price']}""",
        reply_markup=buttons,)







@router.callback_query(F.data.startswith("cart:"))
async def add_to_cart(callback: CallbackQuery):
    dish_id = int(callback.data.split(":")[-1])
    tg_id = callback.from_user.id
    await add_to_card_service(tg_id, dish_id, 1)
    await callback.answer("Товар успешно добавлен в вашу корзинку 👌🏿")



@router.callback_query(F.data.startswith("plus:"))
async def add_to_cart(callback: CallbackQuery):
    dish_id = int(callback.data.split(":")[-1])
    tg_id = callback.from_user.id
    await plus_quantity(dish_id, tg_id)
    await callback.answer("Quantity update successul")



@router.callback_query(F.data.startswith("minus:"))
async def add_to_cart(callback: CallbackQuery):
    dish_id = int(callback.data.split(":")[-1])
    tg_id = callback.from_user.id
    if await minus_quantity(dish_id, tg_id):
        await callback.answer("Опирация успешно виполнено 👌🏿 ")
    else:
        await callback.answer("Количество не модет быт ниже нуля")







@router.callback_query(F.data.startswith("delete:"))
async def add_to_cart(callback: CallbackQuery):
    dish_id = int(callback.data.split(":")[-1])
    tg_id = callback.from_user.id
    await delete_cart_item(dish_id, tg_id)
    await callback.answer("Продукт убран из корзины успешно!!!")




@router.callback_query(F.data.startswith("dish_"))
async def details(callback: CallbackQuery):
    await callback.answer()
    dish_id = int(callback.data.split("_")[-1])
    dish = await get_dish_by_id(dish_id)
    buttons = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Cancel", callback_data="cancel:")]
        ])
    await callback.message.answer_photo(
        photo=dish["photo_file_id"],
        caption=f"""
Title: {dish['title']}
Description:  {dish['description']}
Цена: {dish['price']}""",reply_markup=buttons)




@router.callback_query(F.data.startswith("cancel:"))
async def cancel(callback: CallbackQuery):
    await callback.message.delete()