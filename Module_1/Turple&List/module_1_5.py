immutable_var = 1, True, "tuple", 2.5    # Создание кортежа
print(immutable_var)                    # Вывод кортежа
try:
    immutable_var[0] = 4                # Попытка изменить кортеж
except TypeError:
    print("Тип данных \"tuple\" является неизменяемым")    # Обработка исключения

mutable_var = [2, False, "list", 1.5]   # Создание списка
mutable_var[0] = 5                      # Изменение элемента списка
print(mutable_var)                      # Вывод списка
