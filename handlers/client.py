from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


async def commands_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Чем же вамм помочь?\n\n Ниже вы можете задать свой вопрос', reply_markup=kb_client)
    await sqlite_db.sql_add_users(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)


async def faq(message: types.Message):
    await bot.send_message(message.from_user.id, 'Как работает бот?\n\n '
                                                 '1.Надо задать боту вопрос\n\n '
                                                 '2.Бот сравнит ваш вопрос со списком заготовленных вопросов и при совпадении даст вам ответ\n\n'
                                                 '3.Если ответа на ваш вопрос нету, вы можете нажать кнопку /ASK для того, чтобы отправить заявку специалисту.'
                                                 'Он постарается ответить вам как можно скорее\n\n'
                                                 '4.Вы можете нажать кнопку /Questions для того, чтобы сразу увиидеть всю базу вопросов')


async def ask_operator(message: types.Message):
    await bot.send_message(message.from_user.id, 'В ближайшее время с вами свяжется специалист')
    await bot.send_message('-1001856039852', f'@{message.from_user.username} Хочет задать вопрос')


async def list_of_last_questions(message : types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help', 'start_normal_mode'])
    dp.register_message_handler(faq, commands=['FAQ'])
    dp.register_message_handler(ask_operator, commands=['ASK'])
    dp.register_message_handler(list_of_last_questions, commands=['Questions'])
