my_string = input("Введите текст: ")
print(f"Количество введенных символов: {my_string.__len__()}")
print(my_string.upper())                    # Вывод строки в верхнем регистре
print(my_string.lower())                    # Вывод строки в нижнем регистре
my_string = my_string.replace(" ", "")      # Удаление пробелов в строке
print(my_string[0])                         # Вывод первого символа
print(my_string[my_string.__len__() - 1])   # Вывод последнего символа
