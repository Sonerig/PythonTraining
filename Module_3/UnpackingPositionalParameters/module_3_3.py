def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Задание 1: вызов функций с разным количеством параметров
print_params('Test', 1, False)
print_params(False, 2)
print_params(1.5)
print_params()
# Проверка работы следующих вызовов
print_params(b = 25)
print_params(c = [1,2,3])

# Задание 2: распаковка параметров
values_list = [True, 2.7, 'List']
values_dict = {'a': False, 'b': 7.2, 'c': "Dict"}
# Проверка работы следующих вызовов
print_params(*values_list)
print_params(**values_dict)

# Задание 3: Распаковка + отдельные параметры
values_list_2 = [2.4, 'list_2']
# Проверка работы следующих вызовов
print_params(*values_list_2, 42)
