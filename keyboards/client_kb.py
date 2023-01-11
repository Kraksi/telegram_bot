from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
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


'''Создание инлайн клавиатуры (помогло/не помогло)'''

kb_necessity = InlineKeyboardMarkup()
button_yes = InlineKeyboardButton(text='Да', callback_data='answer_yes')
button_no = InlineKeyboardButton(text='Нет', callback_data='answer_no')
kb_necessity.add(button_yes).add(button_no)

'''Создание дополнительных клавитуы (подкатегорий)'''

'''Подкатегория - Мобильное приложение'''

kb_sub_category_MA = InlineKeyboardMarkup()
button_sub_101 = InlineKeyboardButton(text='Доступ к МП', callback_data='sub_101')
button_sub_102 = InlineKeyboardButton(text='Отправка отчета из МП', callback_data='sub_102')
button_sub_103 = InlineKeyboardButton(text='Проведение УП', callback_data='sub_103')
button_sub_104 = InlineKeyboardButton(text='Сбой в работе МП', callback_data='sub_104')
button_sub_105 = InlineKeyboardButton(text='Сканирование СКМ', callback_data='sub_105')
kb_sub_category_MA.add(button_sub_101).add(button_sub_102).add(button_sub_103).add(button_sub_104).add(button_sub_105)

'''Подкатегория - Учет посещяемости'''

kb_sub_category_AT = InlineKeyboardMarkup()
button_sub_501 = InlineKeyboardButton(text='Подтверждение ведомости', callback_data='sub_501')
button_sub_502 = InlineKeyboardButton(text='Вкладка УП', callback_data='sub_502')
button_sub_503 = InlineKeyboardButton(text='Контроль пропусков занятий', callback_data='sub_503')
button_sub_504 = InlineKeyboardButton(text='Ведомость', callback_data='sub_504')
button_sub_505 = InlineKeyboardButton(text='Отчетные формы для оплаты', callback_data='sub_505')
kb_sub_category_AT.add(button_sub_501).add(button_sub_502).add(button_sub_503).add(button_sub_504).add(button_sub_505)

