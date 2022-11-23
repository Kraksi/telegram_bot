from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from keyboards import category_kb


class FSMAdmin(StatesGroup):
    question = State()
    answer = State()
    category = State()


async def make_changes_command(message: types.Message):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        print(f'Пользователь с id -> {message.from_user.id} подтвержден ')
        await bot.send_message(message.from_user.id, 'Что вы хотите сделать?',
                               reply_markup=admin_kb.button_case_admin_main)
        await bot.send_message(message.from_user.id, 'What do yoy want my lord?', reply_markup=admin_kb.button_case_admin_main)
        await message.delete()


async def accept_the_request(message: types.Message):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        await bot.send_message('-1001856039852', f'{message.from_user.username} Принял запрос')


async def cm_start(message: types.Message):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        await FSMAdmin.question.set()
        await bot.send_message(message.from_user.id, 'Введите вопрос')


async def cancel_handler(message: types.Message, state: FSMContext):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')


async def load_question(message: types.Message, state: FSMContext):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        async with state.proxy() as data:
            data['question'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, 'Введите ответ')


async def load_answer(message: types.Message, state: FSMContext):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        async with state.proxy() as data:
            data['answer'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, 'Введите категорию', reply_markup=category_kb.button_case_category)


'''@dp.callback_query_handler(Text(startswith='Сategory_'))
async def call_category(callback: types.CallbackQuery):
    res = callback.data.split('_')[2]
    print(res)
    await callback.message.answer(text= f'Category: {res}')'''


async def load_category(message: types.Message, state: FSMContext):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        async with state.proxy() as data:
            if message.text =='Мобильное приложение':
                dt = 1
                data['category'] = dt
            elif message.text == 'Учет посещаемости':
                dt = 2
                data['category'] = dt
        await sqlite_db.sql_add_command_questions(state)
        await bot.send_message(message.from_user.id, 'Загрузить еще?', reply_markup=admin_kb.button_case_admin_dop)
        await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Upload', 'Upload_another'])
    dp.register_message_handler(accept_the_request, commands=['Accept_request'])
    dp.register_message_handler(cancel_handler, state="*", commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_question, state=FSMAdmin.question)
    dp.register_message_handler(load_answer, state=FSMAdmin.answer)
    dp.register_message_handler(load_category, state=FSMAdmin.category)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
