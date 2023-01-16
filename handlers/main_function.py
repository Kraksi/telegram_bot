from aiogram import types, Dispatcher
from create_bot import dp, bot
import Livenshtein as liv
from keyboards import kb_client_inline_full, kb_necessity
from data_base import sqlite_db


'''Вывод ответа на вопрос пользователя'''


async def main_function_answer(message: types.Message):
    number = 0
    popular_answer = None
    s = liv.answer_db(message.text)
    popular_answer = liv.pop_answer(s)
    await bot.send_message(message.from_user.id, '--------------------\n\nНаиболее подходящий '
                                                 'ответ:\n\n--------------------')
    await bot.send_message(message.from_user.id, popular_answer[1])
    await bot.send_message(message.from_user.id, '--------------------\n\nПомог ли вам этот '
                                                 'ответ?\n\n--------------------', reply_markup=kb_necessity)
    await sqlite_db.add_quest_answer(message.from_user.id, message.text, popular_answer[1])
    await bot.send_message(message.from_user.id, '--------------------\n\nДругие похожие ответы:'
                                                 '\n\n--------------------')
    for answer in s:
        number += 1
        if number == 1:
            continue
        await bot.send_message(message.from_user.id, f'--------------------\nВопрос: {answer[0]}\n\nОтвет: {answer[1]}\n--------------------')


'''Вывод вопроса о полезности вопроса'''


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('answer_'))
async def answer_necessity(callback):
    flag = callback.data.replace('answer_', '')
    await sqlite_db.add_necessity(callback.from_user.id, flag)
    await bot.send_message(callback.from_user.id, '--------------------\n\nВам помог ответ? Если нет, можете '
                                                  'попробовать сформулировать вопрос по другому или подать запрос на '
                                                  'связь со специалистом\n\n--------------------',
                           reply_markup=kb_client_inline_full)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(main_function_answer)
