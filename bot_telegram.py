from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

'''Запуск бота и запуск базы данных'''
async def on_startup(_):
    print('Bot online')
    sqlite_db.sql_start_q()
    sqlite_db.sql_start_users()

'''Регистрация всех хендлеров'''
from handlers import client, admin, main_function


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
main_function.register_handlers_other(dp)

'''Получение сообщений'''
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
