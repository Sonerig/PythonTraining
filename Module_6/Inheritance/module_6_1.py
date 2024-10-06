class Animal:                       # Класс животного
    def __init__(self, name):       # Определение названия животного
        self.name = name

    alive = True                    # Животное живое
    fed = False                     # Животное накормленное

    def eat(self, food):            # Метод для кормления, принимающий food (объект класса растения)
        if food.edible:             # Если съедобно - съесть
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:                       # Иначе не есть
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:                        # Класс растений
    def __init__(self, name):       # Определение названия растения
        self.name = name

    edible = False                  # Растение съедобное


class Mammal(Animal):               # Дочерний класс от "Животного" - млекопитающее
    pass


class Predator(Animal):             # Дочерний класс от "Животного" - хищник
    pass


class Flower(Plant):                # Дочерний класс от "Растения" - цветы
    pass


class Fruit(Plant):                 # Дочерний класс от "Растения" - фрукты
    edible = True


# Исходные данные
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
