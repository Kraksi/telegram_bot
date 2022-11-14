from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


button_load = KeyboardButton('/Upload')
button_accept = KeyboardButton('/Accept_request')

button_upload_another = KeyboardButton('/Upload_another')
button_start_main_func = KeyboardButton('/Start_normal_mode')

button_case_admin_main = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_accept)
button_case_admin_dop = ReplyKeyboardMarkup(resize_keyboard=True).add(button_upload_another).add(button_accept).add(button_start_main_func)

