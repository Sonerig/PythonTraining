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

    def __len__(self):                                              # Переопределение метода __len__
        return self.number_of_floors

    def __str__(self):                                              # Переопределение метода __str__
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):                                        # Переопределение оператора "=="
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):                                        # Переопределение оператора "<"
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):                                        # Переопределение оператора "<="
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):                                        # Переопределение оператора ">"
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):                                        # Переопределение оператора ">="
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):                                        # Переопределение оператора "!="
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):                                       # Переопределение оператора "+" для self
        return House(self.name, self.number_of_floors + value)      # Пример: h1 + 10 интерпретируется в h1.__add__(10)

    def __iadd__(self, value):                                      # Переопределение оператора "+="
        return self.__add__(value)

    def __radd__(self, value):                                  # Переопределение оператора "+" для value
        return self.__add__(value)                              # Пример: 10 + h2 интерпретируется в 10.__add__(h2)
                                                                # Что в свою очередь интерпретируется в h2.__radd__(10)


# Исходные данные:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)     # __eq__

h1 = h1 + 10        # __add__
print(h1)
print(h1 == h2)

h1 += 10            # __iadd__
print(h1)

h2 = 10 + h2        # __radd__
print(h2)

print(h1 > h2)      # __gt__
print(h1 >= h2)     # __ge__
print(h1 < h2)      # __lt__
print(h1 <= h2)     # __le__
print(h1 != h2)     # __ne__
