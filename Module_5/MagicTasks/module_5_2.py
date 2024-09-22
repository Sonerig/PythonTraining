class House:                                                        # Класс House
    def __init__(self, name, number_of_floors):                     # Конструктор класса принимающий 2 параметра
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):                                     # Метод класса принимающий параметр типа int
        if not isinstance(new_floor, int):                          # Проверка параметра на тип данных
            print("Вводимое значение долно быть целочисленным числом")
        elif new_floor < 1 or new_floor > self.number_of_floors:    # Проверка на доступный диапазон
            print("Такого этажа не существует")
        else:                                                       # Выввод при соблюдении всех условий
            print(*range(1, new_floor + 1))

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


# Исходные данные:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
