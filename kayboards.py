from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from service import *




users_key = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="menu"),KeyboardButton(text="dish")],
        [KeyboardButton(text="cart"), KeyboardButton(text="cancel")],
        [KeyboardButton(text="start"), KeyboardButton(text="help")]

    ],
    resize_keyboard=True
)




admin_key = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="add_dish"),KeyboardButton(text="clear_cart")],
        [KeyboardButton(text="menu"),KeyboardButton(text="dish")],
        [KeyboardButton(text="cart"), KeyboardButton(text="cancel")],
        [KeyboardButton(text="start"), KeyboardButton(text="help")]

    ],
    resize_keyboard=True
)









async def get_delete_dishes_button():
    data = await menu_service()
    keyboards = []
    for i in data:
        keyboards.append([InlineKeyboardButton(text=i["title"],callback_data=f"delete_dish:{i['id']}")])

    keyboards_a1 = InlineKeyboardMarkup(inline_keyboard=keyboards)
    return keyboards_a1






async def get_dish_info_button():
    data = await menu_service()
    keyboards = []
    for i in data:
        keyboards.append([InlineKeyboardButton(text=f"{i['title']}", callback_data=f"dish_{i['id']}")])
    keybor = InlineKeyboardMarkup(inline_keyboard=keyboards)
    return keybor




async def get_dish_button():
    data = await menu_service()
    keyboards = []
    for i in data:
        keyboards.append([InlineKeyboardButton(text=f"{i['title']}", callback_data=f"dish:{i['id']}")])
    keybor = InlineKeyboardMarkup(inline_keyboard=keyboards)
    return keybor
