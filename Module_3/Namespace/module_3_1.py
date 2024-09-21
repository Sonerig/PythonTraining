calls = 0


def count_calls():                                          # Функция-счетчик количеста вызовов функций
    global calls
    calls += 1


def string_info(string_):                                   # Информация о str переменной
    count_calls()
    return len(string_), string_.upper(), string_.lower()


def is_contains(string_, tuple_):                           # Поиск содержащих строк
    count_calls()
    for searching_string in tuple_:
        if searching_string.lower() == string_.lower():
            return True
    return False


# Пример выполняемого кода
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
