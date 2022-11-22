from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, kb_client_inline_start, kb_client_inline_full, markup_inline
from data_base import sqlite_db
from keyboards import category_kb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def filter_text(text):
    question, answer, category, = text
    res = f'-------------------\n\nВопрос: {question}\n\nОтвет: {answer}\n\n-------------------'
    return res


async def commands_start(message: types.Message):
    #    await bot.send_message(message.from_user.id, 'Чем же вамм помочь?\n\n Ниже вы можете задать свой вопрос',
    #                           reply_markup=kb_client)
    await bot.send_message(message.from_user.id, '-------------------\n\nКакой у вас вопрос?\n\nОтправьте этот вопрос '
                                                 'боту и он постарается вам помочь!\n\nТак же через меню вы можете '
                                                 'узнать как работает бот или вывести список всех существующих '
                                                 'вопросов\n\n-------------------',
                           reply_markup=kb_client_inline_start)
    await sqlite_db.sql_add_users(message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                                  message.from_user.username)


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('button_'))
async def menu(call):
    if call.data == 'button_faq':
        await bot.send_message(call.from_user.id, 'Как работает бот?\n\n '
                                                  '1. Надо написать свой вопрос в диалоговое окно бота\n\n '
                                                  '2. Бот сравнит ваш вопрос со списком заготовленных вопросов и при '
                                                  'совпадении даст вам ответ\n\n '
                                                  '3. Если ответа на ваш вопрос нету, вы можете подать запрос для '
                                                  'того, чтобы специалист с вами связался и помог.\n\n '
                                                  '4. Вы можете вывсети список всех существующих вопросов. Если вы не '
                                                  'найти свой вопрос среди них, вы можете сразу подать запрос на '
                                                  'связь со специалистом')
        await bot.send_message(call.from_user.id,
                               '--------------------\n\nПопробуйте задать свой вопрос или посмотрите список всех '
                               'вопросов\n\n--------------------',
                               reply_markup=kb_client_inline_start)
    elif call.data == 'button_questions':
        await bot.send_message(call.from_user.id, 'Выберите категорию', reply_markup=markup_inline)
    elif call.data == 'button_ask':
        await bot.send_message(call.from_user.id,
                               '--------------------\n\nВ ближайшее время с вами свяжется '
                               'специалист\n\n--------------------')
        await bot.send_message('-1001856039852', f'@{call.from_user.username} Хочет задать вопрос')


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('category_'))
async def list_qu(call):
    if call.data == 'category_MA':
        mas_1 = []
        number = 0
        needed_1 = 1
        mas_1 = sqlite_db.sql_read_2(needed_1)
        for q in mas_1:
            number += 1
            await bot.send_message(call.from_user.id, f'Вопрос:\n{q[0]}\n', reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(text='Показать ответ', callback_data=f'show_answer_1_{number}')))
        await bot.send_message(call.from_user.id,
                               '--------------------',
                               reply_markup=kb_client_inline_full)
    elif call.data == 'category_AT':
        mas_2 = []
        number = 0
        needed_2 = 2
        mas_2 = sqlite_db.sql_read_2(needed_2)
        for w in mas_2:
            number += 1
            await bot.send_message(call.from_user.id, f'Вопрос:\n{w[0]}\n', reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(text='Показать ответ', callback_data=f'show_answer_2_{number}')))
        await bot.send_message(call.from_user.id,
                               '--------------------',
                               reply_markup=kb_client_inline_full)


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('show_answer_'))
async def show_answer(callback):
    flag = callback.data[:13]
    category = flag.replace('show_answer_', '')
    mas = sqlite_db.sql_read_2(category)
    str_replace = f'show_answer_{category}_'
    result_data = int(callback.data.replace(str_replace, ''))
    text = None
    for i in range(0, (len(mas)+1)):
        if i == result_data:
            text = await filter_text(mas[i-1])
            await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text = text)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help', 'start_normal_mode'])

