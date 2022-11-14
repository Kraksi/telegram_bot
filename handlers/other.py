from aiogram import types, Dispatcher
from create_bot import dp, bot
import Livenshtein as l
from keyboards import kb_client_inline_full


async def echo_send(message: types.Message):
    number = 0
    popular_answer = None
    s = l.answer_db(message.text)
    popular_answer = l.pop_answer(s)
    await bot.send_message(message.from_user.id, '--------------------\n\nНаиболее подходящий '
                                                 'ответ:\n\n--------------------')
    await bot.send_message(message.from_user.id, popular_answer)
    await bot.send_message(message.from_user.id, '--------------------\n\nДругие похожие ответы:'
                                                 '\n\n--------------------')
    for answer in s:
        number += 1
        if number == 1:
            continue
        await bot.send_message(message.from_user.id, answer)

    await bot.send_message(message.from_user.id, '--------------------\n\nВам помог ответ? Если нет, можете '
                                                 'попробовать сформулировать вопрос по другому или подать запрос на '
                                                 'связь со специалистом\n\n--------------------',
                           reply_markup=kb_client_inline_full)


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)
