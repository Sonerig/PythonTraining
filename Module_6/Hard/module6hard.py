from math import sqrt, pi


class Figure:
    def __init__(self, color, *sides):
        self.sides_count = 0
        self.__sides = sides
        self.__color = color
        self.filled = bool()

    def get_color(self):
        return self.__color

    def __is_valid_color(self, new_color):
        for item in new_color:
            if not isinstance(item, int):
                return False
            elif not 0 <= item <= 255:
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color([r, g, b]):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != len(self.__sides):
            return False
        else:
            for side in new_sides:
                if not (isinstance(side, int) and side > 0):
                    return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimeter = 0
        for side in self.__sides:
            perimeter += side

        return perimeter

    def set_sides(self, *new_sides, new_object=False):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
        elif isinstance(self, Cube) and len(new_sides) == 1:
            for i in range(self.sides_count):
                self.__sides += (new_sides[0],)
        elif new_object:
            self.__sides = tuple()
            for i in range(self.sides_count):
                self.__sides += (1,)


class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 1
        super().set_sides(*sides, new_object=True)
        self.__radius = self.get_radius(sides[0])

    def get_radius(self, circumference):
        return circumference / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 3
        super().set_sides(*sides, new_object=True)

    def get_square(self):
        sides = super().get_sides()
        p = (sides[0] + sides[1] + sides[2]) / 2
        return sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 12
        super().set_sides(*sides, new_object=True)

    def get_volume(self):
        sides = super().get_sides()
        return int(sides[0]) ** 3


# Исходные данные
circle1 = Circle((200, 200, 100), 10)   # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((160, 120, 200), 1, 4, 2)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)           # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)            # Не изменится
print(cube1.get_color())
triangle1.set_color(255, 130, 15)       # Изменится
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)         # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)                   # Изменится
print(circle1.get_sides())
triangle1.set_sides(12, 12, 12)         # Изменится
print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина, и его площади:
print(len(circle1))
print(circle1.get_square())

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади треугольника:
print(triangle1.get_square())
