# import os
from fuzzywuzzy import fuzz
from data_base import sqlite_db

mas = []
funcs = [fuzz.ratio, fuzz.token_sort_ratio, fuzz.partial_ratio, fuzz.token_set_ratio, fuzz.UWRatio,
         fuzz.partial_token_set_ratio, fuzz.partial_token_sort_ratio, fuzz.QRatio, fuzz.WRatio]


def sort_questions(list_of_questions):
    list_of_questions.sort(reverse=True)
    result_list = []
    final_list = []
    number_of_elements = 0
    for item in list_of_questions:
        number_of_elements += 1
    if number_of_elements > 3:
        for i in range(0, 3):
            result_list.append(list_of_questions[i])
    elif number_of_elements == 3:
        for i in range(0, 2):
            result_list.append(list_of_questions[i])
    elif number_of_elements == 2:
        result_list.append(list_of_questions[0])
    elif number_of_elements == 1:
        result_list.append(list_of_questions[0])
    for ans in result_list:
        final_list.append(ans[1])
    return final_list


def get_coef(questions, text):
    coef_max = 0
    coef_oth = 0
    result_for_list = None
    answer = None
    list_q = []
    for question in questions:
        coef_cur = 0
        for quest in question:
            for f in funcs:
                coef_cur += f(quest, text)
        if ((coef_cur > coef_max) or (coef_cur > (coef_oth - 300))):
            coef_max = coef_cur
            coef_oth = coef_max
            answer = question[1]
            result_for_list = [coef_max, answer]
            list_q.append(result_for_list)

    #    return answer
    return list_q


def answer_db(text):
    answer = []
    text = text.lower().strip()
    mas = sqlite_db.sql_read_1()
    answer = sort_questions(get_coef(mas, text))

    #    return f'Ваш ответ:\n{answer}'
    return answer


def pop_answer(l):
    popular_answer = None
    num = 0
    for qu in l:
        if num == 0:
            popular_answer = qu
            num += 1
    return popular_answer
