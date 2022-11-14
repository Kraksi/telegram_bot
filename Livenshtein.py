# import os
from fuzzywuzzy import fuzz
from data_base import sqlite_db

mas = []
funcs = [fuzz.ratio, fuzz.token_sort_ratio, fuzz.partial_ratio, fuzz.token_set_ratio, fuzz.UWRatio,
         fuzz.partial_token_set_ratio, fuzz.partial_token_sort_ratio, fuzz.QRatio, fuzz.WRatio]


def get_coef(questions, text):
    coef_max = 0
    answer = None
    for question in questions:
        coef_cur = 0
        for quest in question:
            for f in funcs:
                coef_cur += f(quest.replace('u:', ''), text)
        if coef_cur > coef_max:
            coef_max = coef_cur
            answer = question[1]
    print(coef_max)
    return answer


def answer_db(text):
    text = text.lower().strip()
    mas = sqlite_db.sql_read_1()
    answer = get_coef(mas, text)

    return f'Ваш ответ:\n{answer}'
