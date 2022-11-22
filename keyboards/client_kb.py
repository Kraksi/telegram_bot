from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

'''Создание обычной клавиатуры'''

b1 = KeyboardButton('/FAQ')
b2 = KeyboardButton('/ASK')
b3 = KeyboardButton('/Questions')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).insert(b2).add(b3)

'''Создание инлайн клавиатуры общего меню'''

kb_client_inline_start = InlineKeyboardMarkup()
kb_client_inline_full = InlineKeyboardMarkup()
button_faq = InlineKeyboardButton(text='Как работает бот', callback_data='button_faq')
button_ask = InlineKeyboardButton(text='Обратиться к оператору', callback_data='button_ask')
button_questions = InlineKeyboardButton(text='Вывести существующий список вопросов', callback_data='button_questions')
kb_client_inline_start.add(button_faq).add(button_questions)
kb_client_inline_full.add(button_ask).add(button_faq).insert(button_questions)

'''Создание инлайн клавиатуры для категорий'''

markup_inline = InlineKeyboardMarkup()
item_MA = InlineKeyboardButton(text='Мобильное приложение', callback_data='category_MA')
item_AT = InlineKeyboardButton(text='Учет посещаемости', callback_data='category_AT')
markup_inline.add(item_AT).add(item_MA)



