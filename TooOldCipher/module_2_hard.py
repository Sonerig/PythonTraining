from random import randint                              # Импорт рандомайзера

random_num = randint(3, 20)                             # Исходное число
result = str()                                          # Дальнейший результат
for i in range(1, 20):                                  # Цикл перебора чисел
    for j in range(i + 1, 20):                          # Цикл перебора чисел
        if random_num % (i + j) == 0:
            result += str(i) + '+' + str(j) + ' '       # Добавление подходящей пары в результат
print(f"Исходное число: {random_num}\nШифр: {result}")  # Вывод результата
