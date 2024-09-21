first = input("First num: ")    # Ввод первого числа
second = input("Second num: ")  # Ввод второго числа
third = input("Third num: ")    # Ввод третьего числа

if first == second and first == third:
    print("3")  # Вывод при условии что все числа равны
elif first == second or first == third or second == third:
    print("2")  # Вывод при условии что хотя бы 2 чисела равны
else:
    print("0")  # Вывод при условии что равных чисел нет
