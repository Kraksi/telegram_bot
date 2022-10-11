from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


button_load = KeyboardButton('/Upload')
button_delete = KeyboardButton('/Accept_request')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)


