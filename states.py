from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from service import *
from kayboards import *
from aiogram.types import CallbackQuery


router = Router()



@router.message(F.text == "cancel")
@router.message(Command("cancel"))
async def cancel_input(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Ваша операция отменена")




class Add_dish(StatesGroup):
    get_title = State()
    get_price = State()
    get_description = State()
    get_photo_file_id = State()









@router.message(F.text == "add_dish")
@router.message(Command("add_dish"))
async def start_get_information(message : Message , state : FSMContext):
    status = await check_admin(message.from_user.id)
    if status:
        await message.answer("Введите название товара: ")
        await state.set_state(Add_dish.get_title)
    else:
        print("ты не админ уйди отсюда")
        await state.clear()

@router.message(Add_dish.get_title)
async def get_title_state(message : Message , state : FSMContext):
    await state.update_data(title = message.text)
    await message.answer("Введите цену товара: ")
    await state.set_state(Add_dish.get_price)


@router.message(Add_dish.get_price)
async def get_price_state(message : Message , state : FSMContext):
    try:
        price = int(message.text)
        if price <=0:
            return await message.answer("Цуна должно не может быт отрицателным")
        await state.update_data(price = price)
        await message.answer("Введите описание товара: ")
        await state.set_state(Add_dish.get_description)
    except:
        return await message.answer("Ошибка ввода попытайтесъ снова: ")


@router.message(Add_dish.get_description)
async def het_title_state(message : Message , state : FSMContext):
    await state.update_data(description = message.text)
    await message.answer("Скинте фото товара пожалуйста: ")
    await state.set_state(Add_dish.get_photo_file_id)

@router.message(Add_dish.get_photo_file_id)
async def get_file_photo_id_state(message : Message , state : FSMContext):
    if not message.photo:
            await message.answer("Вы отправили не фото пожайлусто отправте фото блюда")
            return None
    photo = message.photo[-1]
    await state.update_data(file_id = photo.file_id)
    data = await state.get_data()
    if await add_dish_service(data['title'], data['price'], data['description'], data['file_id']):
        await message.answer("Блюдо добавлено удачно")
    else:
        await message.answer("При добовлении блюда произошла ошибка")
    await state.clear()












@router.message(F.text == "menu")
@router.message(Command("menu"))
async def menu(message: Message):
    dishes = await menu_service()
    if not dishes:
        return await message.answer("Сорян покачто наш могозин пуст🏪")

    for dish in dishes:
        buttons = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Подробнее",
                    callback_data=f"dish:{dish['id']}"
                ),
                InlineKeyboardButton(
                    text="🛒 Добавить",
                    callback_data=f"cart:{dish['id']}"
                ),
                InlineKeyboardButton(
                    text="➕",
                    callback_data=f"plus:{dish['id']}"
                ),
                InlineKeyboardButton(
                    text="➖",
                    callback_data=f"minus:{dish['id']}"
                ),
                    InlineKeyboardButton(
                    text="🗑 Удалить",
                    callback_data=f"delete:{dish['id']}"
                )
                
            ]
        ])

        await message.answer(dish["title"], reply_markup=buttons)











@router.message(F.text == "cart")
@router.message(Command("cart"))
async def show_cart(message: Message):
    data = await show_cart_service(message.from_user.id)
    total = 0
    await message.answer("Твоя корзина")
    for i in data:
        cost = i["price"] * i["quantity"]
        total += cost

        await message.answer(f"""
Продукт: {i['title']}
Цена: {i['price']}
Количество: {i['quantity']}
        """)

    await message.answer(f"💰 Общая стоимость: {total} сомони")






















# ======================