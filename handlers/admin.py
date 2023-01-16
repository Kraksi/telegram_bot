from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import ContentTypes

from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from keyboards import markup_inline_ad
import work_with_excel


class FSMAdmin(StatesGroup):
    question = State()
    answer = State()
    category = State()


'''-----------------------------------------Подтверждение админа----------------------------------------------------'''


async def make_changes_command(message: types.Message):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        print(f'Пользователь с id -> {message.from_user.id} подтвержден ')
        await bot.send_message(message.from_user.id, 'Что вы хотите сделать?',
                               reply_markup=admin_kb.button_case_admin_main)
        await bot.send_message(message.from_user.id, 'What do yoy want my lord?', reply_markup=admin_kb.button_case_admin_main)
        await message.delete()


'''Обработчик загрузки файла'''


async def ask_for_file(message: types.Message):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        await bot.send_message(message.from_user.id, 'Пожалуйста приложите файл формата .xlsx', reply_markup=admin_kb.button_case_admin_main)


'''------------------------------------Модуль загрузки большого колличества-----------------------------------------'''


@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def upload_many_questions(message: types.Message):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
            print("downloading document")
            destination = r"C:\Users\Krasti\Desktop\telegram_bot\file.xlsx"
            destination_file = await message.document.download(destination_file=destination)
            work_with_excel.openxlsx()
            print("success in bot")


'''------------------------------------Оповещение о принятия запроса------------------------------------------------'''


async def accept_the_request(message: types.Message):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        await bot.send_message('-1001856039852', f'{message.from_user.username} Принял запрос')


'''-----------Начало машины состояний для ввода нового вопроса с инлайн клавитурой для выбора категории-------------'''


async def cm_start(message: types.Message):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        await bot.send_message(message.from_user.id, 'Выберите категорию', reply_markup=markup_inline_ad)


'''----------------------------------------------Выбор подкатегории-------------------------------------------------'''


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('admin_category_'))
async def add_cat(call):
    if call.data == 'admin_category_MA':
        await bot.send_message(call.from_user.id,
                               'Выберите подкатегорию', reply_markup=admin_kb.kb_adm_category_MA)

    elif call.data == 'admin_category_AT':
        await bot.send_message(call.from_user.id,
                               'Выберите подкатегорию', reply_markup=admin_kb.kb_adm_category_AT)


'''----------------------------------Добавление в буфер выбранной подкатегории--------------------------------------'''


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('adm_'))
async def add_sub_cat(call):
    needed = call.data.replace('adm_', '')
    need = int(needed)
    await sqlite_db.add_buf_info(call.from_user.id, need)
    check = False
    check = await sqlite_db.check_user_id(call.from_user.id)
    if check:

        await bot.send_message(call.from_user.id, 'Введите вопрос')
        await FSMAdmin.question.set()


'''---------------------------------------Отсановка машины состояний------------------------------------------------'''


async def cancel_handler(message: types.Message, state: FSMContext):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    if check:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')


'''---------------------------------------------Ввод вопроса--------------------------------------------------------'''


async def load_question(message: types.Message, state: FSMContext):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    cat = await sqlite_db.read_cat(message.from_user.id)
    if check:
        async with state.proxy() as data:
            data['question'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, 'Введите ответ')


'''---------------------------------------------Ввод ответа---------------------------------------------------------'''


async def load_answer(message: types.Message, state: FSMContext):
    check = False
    check = await sqlite_db.check_user_id(message.from_user.id)
    cat = await sqlite_db.read_cat(message.from_user.id)
    if check:
        async with state.proxy() as data:
            data['answer'] = message.text
            data['category'] = cat
            await sqlite_db.delete_buf(message.from_user.id)
        await sqlite_db.sql_add_command_questions(state)
        await bot.send_message(message.from_user.id, 'Загрузить еще?', reply_markup=admin_kb.button_case_admin_dop)
        await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Upload', 'Upload_another'])
    dp.register_message_handler(accept_the_request, commands=['Accept_request'])
    dp.register_message_handler(cancel_handler, state="*", commands='cancel')
    dp.register_message_handler(ask_for_file, commands=['Upload_many_questions'])
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_question, state=FSMAdmin.question)
    dp.register_message_handler(load_answer, state=FSMAdmin.answer)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
