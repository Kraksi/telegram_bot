from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_load = KeyboardButton('/Upload')
button_upload_many = KeyboardButton('/Upload_many_questions')
button_accept = KeyboardButton('/Accept_request')


button_upload_another = KeyboardButton('/Upload_another')
button_start_main_func = KeyboardButton('/Start_normal_mode')

button_case_admin_main = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_accept).add(button_upload_many)
button_case_admin_dop = ReplyKeyboardMarkup(resize_keyboard=True).add(button_upload_another).add(button_accept).add(button_start_main_func)

'''Создание дополнительных клавитур (подкатегорий) для админа'''

'''Подкатегория - Мобильное приложение'''

kb_adm_category_MA = InlineKeyboardMarkup()
button_adm_101 = InlineKeyboardButton(text='Доступ к МП', callback_data='adm_101')
button_adm_102 = InlineKeyboardButton(text='Отправка отчета из МП', callback_data='adm_102')
button_adm_103 = InlineKeyboardButton(text='Проведение УП', callback_data='adm_103')
button_adm_104 = InlineKeyboardButton(text='Сбой в работе МП', callback_data='adm_104')
button_adm_105 = InlineKeyboardButton(text='Сканирование СКМ', callback_data='adm_105')
kb_adm_category_MA.add(button_adm_101).add(button_adm_102).add(button_adm_103).add(button_adm_104).add(button_adm_105)

'''Подкатегория - Учет посещяемости'''

kb_adm_category_AT = InlineKeyboardMarkup()
button_adm_501 = InlineKeyboardButton(text='Подтверждение ведомости', callback_data='adm_501')
button_adm_502 = InlineKeyboardButton(text='Вкладка УП', callback_data='adm_502')
button_adm_503 = InlineKeyboardButton(text='Контроль пропусков занятий', callback_data='adm_503')
button_adm_504 = InlineKeyboardButton(text='Ведомость', callback_data='adm_504')
button_adm_505 = InlineKeyboardButton(text='Отчетные формы для оплаты', callback_data='adm_505')
kb_adm_category_AT.add(button_adm_501).add(button_adm_502).add(button_adm_503).add(button_adm_504).add(button_adm_505)

'''Создание инлайн клавиатуры для категорий админ'''

markup_inline_ad = InlineKeyboardMarkup()
item_MA_ad = InlineKeyboardButton(text='Мобильное приложение', callback_data='admin_category_MA')
item_AT_ad = InlineKeyboardButton(text='Учет посещаемости', callback_data='admin_category_AT')
markup_inline_ad.add(item_AT_ad).add(item_MA_ad)