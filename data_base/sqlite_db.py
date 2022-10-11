import sqlite3 as sq
from create_bot import dp, bot


def sql_start():
    global base, cur
    base = sq.connect('list_q_a.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS list_q_a(question TEXT PRIMARY KEY, answer TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO list_q_a VALUES (?,?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM list_q_a').fetchall():
        await bot.send_message(message.from_user.id, f'Вопрос: {ret[0]}\nОтвет: {ret[1]}')


def sql_read_1():
    cur.execute('SELECT * FROM list_q_a')
    return cur.fetchall()

