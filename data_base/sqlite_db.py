import sqlite3 as sq
from create_bot import dp, bot
from datetime import date, datetime


'''----------------------------------------Создание базы данных для вопросов----------------------------------------'''


def sql_start_q():
    global base_q, cur_q
    base_q = sq.connect('list_q_a.db')
    cur_q = base_q.cursor()
    if base_q:
        print('Questions data base connected OK!')
    base_q.execute('CREATE TABLE IF NOT EXISTS list_q_a(question TEXT PRIMARY KEY, answer TEXT, category INT)')
    base_q.commit()
    base_q.execute(
        'CREATE TABLE IF NOT EXISTS list_q_a_user(data TEXT, id TEXT, question TEXT, answer TEXT, necessity TEXT)')
    base_q.execute('CREATE TABLE IF NOT EXISTS buf_store(id TEXT, category INT)')
    base_q.commit()


'''-----------------------------------Создание базы данных для пользователей----------------------------------------'''


def sql_start_users():
    global base_u, cur_u
    base_u = sq.connect('users.db')
    cur_u = base_u.cursor()
    if base_u:
        print('Users data base connected OK!')
    base_u.execute(
        'CREATE TABLE IF NOT EXISTS users(user_id TEXT PRIMARY KEY, user_name TEXT, user_second_name TEXT, user_nickname TEXT)')
    base_u.commit()
    base_u.execute('CREATE TABLE IF NOT EXISTS allowed_users(user_id TEXT PRIMARY KEY, user_name TEXT)')
    base_u.commit()


'''-------------------------------------Добавление новых вопросов (админ)-------------------------------------------'''


async def sql_add_command_questions(state):
    async with state.proxy() as data:
        cur_q.execute('INSERT INTO list_q_a VALUES (?,?,?)', tuple(data.values()))
        base_q.commit()


'''--------------------------------Сохранение истории кто пользовался ботом-----------------------------------------'''


async def sql_add_users(message_chat_id, message_user_name, message_user_second_name, message_user_nickname):
    user_data = [message_chat_id, message_user_name, message_user_second_name, message_user_nickname]
    people_id = message_chat_id
    cur_u.execute(f'SELECT user_id FROM users WHERE user_id = {people_id}')
    data = cur_u.fetchone()
    if data is None:
        cur_u.execute('INSERT INTO users VALUES (?,?,?,?);', user_data)
        base_u.commit()





async def sql_read(message):
    for ret in cur_q.execute('SELECT * FROM list_q_a').fetchall():
        await bot.send_message(message.from_user.id, f'Вопрос:\n{ret[0]}\nОтвет:\n{ret[1]}')


'''-------------------------------Считываение всех вопросов из базы данных------------------------------------------'''


def sql_read_1():
    cur_q.execute('SELECT * FROM list_q_a')
    return cur_q.fetchall()


'''--------------------------Считываение вопросов по категории из базы данных---------------------------------------'''


def sql_read_2(category):
    mas = []
    cur_q.execute(f'SELECT * FROM list_q_a WHERE category = {category}')
    mas = cur_q.fetchall()
    return mas


'''---------------------------------Проверка пользователя на админа-------------------------------------------------'''


async def check_user_id(id_user):
    boolean = False
    array_users = []
    cur_u.execute('SELECT user_id FROM allowed_users')
    array_users = cur_u.fetchall()
    for user in array_users:
        buf, = user
        id = int(buf)
        if id == id_user:
            boolean = True
    if not boolean:
        print('Сторонний пользователь попытался воспользоваться ботом')
    return boolean


async def add_quest_answer(id_user, quest, answer):
    data = datetime.today()
    cur_q.execute(
        f"INSERT INTO list_q_a_user (data, id, question, answer) VALUES ('{data}','{id_user}','{quest}','{answer}')")
    base_q.commit()


async def add_necessity(id_user, necessity):
    cur_q.execute(
        f"UPDATE list_q_a_user SET necessity = '{necessity}' WHERE data IN (SELECT data FROM list_q_a_user ORDER BY data DESC LIMIT 1)")
    base_q.commit()


''' '''


async def read_quest(id_user):
    cur_q.execute(f"SELECT question FROM list_q_a_user WHERE id = '{id_user}' ORDER BY data DESC LIMIT 1")
    res = cur_q.fetchone()
    return res


'''------------------------------------------Создание буфера данных-------------------------------------------------'''


async def add_buf_info(id_creator, needed):
    cur_q.execute(f"INSERT INTO buf_store (id, category) VALUES ('{id_creator}','{needed}')")
    base_q.commit()


'''--------------------------------------Считывание данных из буфера------------------------------------------------'''


async def read_cat(id_user):
    array_name = []
    result = None
    id_u = None
    array_name = cur_q.execute('SELECT * FROM buf_store').fetchall()
    for user_data in array_name:
        id_u, category_u, = user_data
        id_use = int(id_u)
        if id_use == id_user:
            if category_u != 'NULL':
                result = category_u
    return result


'''--------------------------------------Удаление буфера данных-----------------------------------------------------'''


async def delete_buf(id_user):
    cur_q.execute(f'DELETE FROM buf_store WHERE id = {id_user}')
    base_q.commit()