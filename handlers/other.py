from aiogram import types, Dispatcher
from create_bot import dp, bot
import Livenshtein as l
from keyboards import kb_client_inline_full

async def echo_send(message: types.Message):

    s = l.answer_db(message.text)
    await bot.send_message(message.from_user.id, s)
    await bot.send_message(message.from_user.id, '--------------------\n\nВам помог ответ? Если нет, можете '
                                                 'попробовать сформулировать вопрос по другому или подать запрос на '
                                                 'связь со специалистом\n\n--------------------',
                           reply_markup=kb_client_inline_full)


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)
