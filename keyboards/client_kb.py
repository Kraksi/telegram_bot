from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/FAQ')
b2 = KeyboardButton('/ASK')
b3 = KeyboardButton('/Questions')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b2).add(b3)