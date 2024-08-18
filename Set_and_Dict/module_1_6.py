# Работа со словарями
my_dict = {"Ivan": 2003, "Stepan": 1995, "Andrey": 2000}    # Создание словаря
print(my_dict)                                              # Вывод словаря
print(my_dict.get("Andrey"))                                # Вывод значения по существующему ключу
print(my_dict.get("Alex", "The key is not found"))          # Вывод значения по несуществующему ключу
my_dict.update({"Alex": 2001, "David": 2004})               # Добавление двух пар
PopFromDict = my_dict.pop("Stepan")                         # Удаление пары
print(PopFromDict)                                          # Вывод удаленной пары
print(my_dict)                                              # Вывод словаря

# Работа с множествами
my_set = {1, 3, "Set", "Set", 3, 1}     # Создание множества
print("Множество: ", my_set)            # Вывод множества
my_set.update([False, 2])               # Добваление двух жлементов в множество
my_set.discard("Set")                   # Удаление элемента из множества
print(my_set)                           # Вывод измененного множества
