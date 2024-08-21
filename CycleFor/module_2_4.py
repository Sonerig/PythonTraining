numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]   # Исходный список

primes = list()                                                 # Список простых чисел
not_primes = list()                                             # Список не простых чисел
is_prime = True                                                 # Флаг простого числа

for i in numbers:                                               # Цикл пробегающий по списку
    if i == 1:
        continue                                                # Пропустить итерацию если числом является единица

    for j in range(2, i):                                       # Цикл для деления на числа от 2 до i (текущего числа)
        if i % j == 0:
            is_prime = False                                    # Флаг в положение False, если число не простое
            break                                               # Остановка цикла, т. к. известно что число не простое

    if is_prime:                                                # Проверка числа по флагу
        primes.append(i)                                        # Добавить число в список простых чисел если оно простое
    else:
        not_primes.append(i)                                    # Добавить в список не простых чисел если оно не простое

    is_prime = True                                             # Обновление флага в положение True

print(f"Primes: {primes}")                                      # Вывод простых чисел
print(f"Not primes: {not_primes}")                              # Вывод не простых чисел
