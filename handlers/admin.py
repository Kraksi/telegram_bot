from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb

ID = None


class FSMAdmin(StatesGroup):
    question = State()
    answer = State()


#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'What do yoy want my lord?', reply_markup=admin_kb.button_case_admin)
    await message.delete()


async def accept_the_request(message : types.Message):
    if message.from_user.id == ID:
        await bot.send_message('-1001856039852', f'{message.from_user.username} Принял запрос')


#@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.question.set()
        await bot.send_message(message.from_user.id, 'Введите вопрос')


#@dp.message_handler(state="*", commands='cancel')
#@dp.message_handler(Text(equals='cancel', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')


#@dp.message_handler(state=FSMAdmin.question)
async def load_question(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['question'] = f'u:{message.text}'
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, 'Введите ответ')
#        await message.reply("Теперь введите ответ")


#@dp.message_handler(state=FSMAdmin.answer)
async def load_answer(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['answer'] = message.text
#        async with state.proxy() as data:
#            await message.reply(str(data))
        await sqlite_db.sql_add_command(state)
        await state.finish()



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Upload'])
    dp.register_message_handler(accept_the_request, commands=['Accept_request'])
    dp.register_message_handler(cancel_handler, state="*", commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_question, state=FSMAdmin.question)
    dp.register_message_handler(load_answer, state=FSMAdmin.answer)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)











