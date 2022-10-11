def translate(message):

    str = message
    result_1 = str.replace('/', '')
    result = result_1.replace('_', ' ')
    print(result)
    return result
