from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


button_AT = KeyboardButton('Учет посещаемости')
button_MA = KeyboardButton('Мобильное приложение')


button_case_category = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_AT).add(button_MA)