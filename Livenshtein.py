#import os
from fuzzywuzzy import fuzz
from data_base import sqlite_db

mas = []
''' Старые функции через файл
if os.path.exists('Questions.txt'):
    f = open('Questions.txt', 'r', encoding='UTF-8')
    for x in f:
        if (len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()

def answer(text):
    try:
        text = text.lower().strip()
        if os.path.exists('Questions.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if ('u: ' in q):
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    aa = (fuzz.token_sort_ratio(q.replace('u: ', ''), text))
                    if (aa > a and aa != a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'
'''
def answer_db(text):
    try:
        text = text.lower().strip()
        mas = sqlite_db.sql_read_1()
        a_max_coef = 0
        answer = -1
        for q in mas:
            # С помощью fuzzywuzzy получаем, насколько похожи две строки
#            a_cur_coef = (fuzz.token_sort_ratio(q[0].replace('u:', ''), text))
            a_cur_coef = (fuzz.ratio(q[0].replace('u:', ''), text))
            if (a_cur_coef > a_max_coef and a_cur_coef != a_max_coef):

                a_max_coef = a_cur_coef
                answer = q
        return f'Ваш ответ:\n{answer[1]}'
    except:
        return 'Ошибка'