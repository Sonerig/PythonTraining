class Horse:
    x_distance = 0
    sound = "Frrr"

    def run(self, dx, dy):
        Horse.x_distance += dx
        super().fly(dy)

    def voice(self):
        return super().sound


class Eagle:
    y_distance = 0
    sound = "I train, eat, sleep, and repeat"

    def fly(self, dy):
        Eagle.y_distance += dy


class Pegasus(Horse, Eagle):
    def voice(self):
        print(super().voice())

    def move(self, dx, dy):
        super().run(dx, dy)

    def get_pos(self):
        return super().x_distance, super().y_distance


# Исходные данные
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
