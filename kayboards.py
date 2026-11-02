from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from service import *




users_key = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='cancel')], [KeyboardButton(text='cart')], [KeyboardButton(text='help')], [KeyboardButton(text='menu')], [KeyboardButton(text='start')]], resize_keyboard=True)




admin_key = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='add_dish')], [KeyboardButton(text='cancel')], [KeyboardButton(text='cart')], [KeyboardButton(text='help')], [KeyboardButton(text='menu')], [KeyboardButton(text='start')]], resize_keyboard=True)















