from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db
from keyboards import category_kb

mas_1 = []
mas_2 = []
async def commands_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Чем же вамм помочь?\n\n Ниже вы можете задать свой вопрос',
                           reply_markup=kb_client)
    await sqlite_db.sql_add_users(message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                                  message.from_user.username)


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


async def list_of_last_questions(message: types.Message):
#    await bot.send_message(message.from_user.id, 'Выберите категорию', reply_markup=category_kb.button_case_category_c)
    markup_inline = types.InlineKeyboardMarkup()
    item_MA = types.InlineKeyboardButton(text='Мобильное приложение', callback_data='category_MA')
    item_AT = types.InlineKeyboardButton(text='Учет посещаемости', callback_data='category_AT')
    markup_inline.add(item_AT).add(item_MA)
    await bot.send_message(message.from_user.id, 'Выберите категори', reply_markup=markup_inline)

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('category_'))
async def list_qu(call):
    if call.data =='category_MA':
        needed_1 = 1
        mas_1 = sqlite_db.sql_read_2(needed_1)
        for q in mas_1:
            await bot.send_message(call.from_user.id, f'Вопрос:\n{q[0]}\n\nОтвет:\n{q[1]}')


    elif call.data =='category_AT':
        needed_2 = 2
        mas_2 = sqlite_db.sql_read_2(needed_2)
        for w in mas_2:
            await bot.send_message(call.from_user.id, f'Вопрос:\n{w[0]}\n\nОтвет:\n{w[1]}')

#async def choose_questions_from_list(message: types.Message):
#    await sqlite_db.sql_read_2(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help', 'start_normal_mode'])
    dp.register_message_handler(faq, commands=['FAQ'])
    dp.register_message_handler(ask_operator, commands=['ASK'])
    dp.register_message_handler(list_of_last_questions, commands=['Questions'])
#    dp.register_message_handler(choose_questions_from_list, commands=["""/Учет_посещаемости""", """/Мобильное_приложение"""])
