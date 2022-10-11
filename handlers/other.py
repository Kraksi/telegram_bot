from aiogram import types, Dispatcher
from create_bot import dp, bot
import Livenshtein as l


# @dp.message_handler()
async def echo_send(message: types.Message):

    s = l.answer_db(message.text)
    await bot.send_message(message.from_user.id, s)

#    await bot.send_message('131144684', message.text)


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)
