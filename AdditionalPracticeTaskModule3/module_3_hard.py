def sum_of_data_struct(*data, **dict_data):     # Функция подсчета всех элементов и длин строк
    result = 0                                  # Переменная с будущим результатом

    for key, value in dict_data.items():        # Вычисление длин ключей словарей и их значений
        result += len(key) + value

    for i in data:
        if isinstance(i, str):
            result += len(i)                    # Добавление длины строки
        elif isinstance(i, dict):
            result += sum_of_data_struct(**i)   # Рекурсия для вычисления словарей
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            result += sum_of_data_struct(*i)    # Рекурсия для вычисления массива данных
        else:
            result += i                         # Добавление текущего элемента в ином случае
    return result


data_structure = [                              # Список с исходными данными
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(sum_of_data_struct(*data_structure))      # Вызов функции вычисления суммы всех элементов и длин строк
