def get_multiplied_number(number):                                          # Функция умножения цифр в числе
    number = str(number).replace('0', '')                                   # Удаление нулей в полученом числе
    if len(number) > 1:
        return int(number[0]) * get_multiplied_number(int(number[1:]))      # Рекурсия, если цифр больше чем 1
    return int(number[0])                                                   # Возврат последнего числа


print(get_multiplied_number(int(input("The num: "))))                       # Вывод итога, вызов функции, ввод числа
