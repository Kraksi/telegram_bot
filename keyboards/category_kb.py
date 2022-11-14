from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


button_AT = KeyboardButton('Учет посещаемости')
button_MA = KeyboardButton('Мобильное приложение')

button_AT_c = KeyboardButton('/Учет_посещаемости')
button_MA_c = KeyboardButton('/Мобильное_приложение')

button_case_category = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_AT).add(button_MA)
button_case_category_c = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_AT_c).add(button_MA_c)