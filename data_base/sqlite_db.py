import sqlite3 as sq
from create_bot import dp, bot


def sql_start_q():
    global base_q, cur_q
    base_q = sq.connect('list_q_a.db')
    cur_q = base_q.cursor()
    if base_q:
        print('Questions data base connected OK!')
    base_q.execute('CREATE TABLE IF NOT EXISTS list_q_a(question TEXT PRIMARY KEY, answer TEXT)')
    base_q.commit()

def sql_start_users():
    global base_u, cur_u
    base_u = sq.connect('users.db')
    cur_u = base_u.cursor()
    if base_u:
        print('Users data base connected OK!')
    base_u.execute('CREATE TABLE IF NOT EXISTS users(user_id TEXT PRIMARY KEY, user_name TEXT, user_second_name TEXT, user_nickname TEXT)')
    base_u.commit()

async def sql_add_command_questions(state):
    async with state.proxy() as data:
        cur_q.execute('INSERT INTO list_q_a VALUES (?,?)', tuple(data.values()))
        base_q.commit()


async def sql_add_users(message_chat_id, message_user_name, message_user_second_name, message_user_nickname):
    user_data = [message_chat_id, message_user_name, message_user_second_name, message_user_nickname]
    people_id = message_chat_id
    cur_u.execute(f'SELECT user_id FROM users WHERE user_id = {people_id}')
    data = cur_u.fetchone()
    if data is None:
        cur_u.execute('INSERT INTO users VALUES (?,?,?,?);', user_data)
        base_u.commit()
    else:
        print('Уже есть такой пользователь')


async def sql_read(message):
    for ret in cur_q.execute('SELECT * FROM list_q_a').fetchall():
        await bot.send_message(message.from_user.id, f'Вопрос: {ret[0]}\nОтвет: {ret[1]}')


def sql_read_1():
    cur_q.execute('SELECT * FROM list_q_a')
    return cur_q.fetchall()

