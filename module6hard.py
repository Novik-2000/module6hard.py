import math


class Figure:
    sides_count = 0

    def __init__(self, __sides, __color):
        self.__sides = __sides
        self.__color = [0, 0, 0]

    def get_color(self):
        return self.__color
    def set_color(self, r=0, g=0, b=0):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_color(self, r, g, b):
        if 0 <= isinstance([r, g, b], int) <= 225:
            return True
        else:
            return False

    def __is_valid_sides(self, __sides):
        if __sides > 0 and __sides == self.__sides:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if new_sides != self.sides_count:
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.__sides * (2 / math.pi)

    def get_square(self):
        return self.__radius() / (4 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def get_square(self, p):
        self.p = 0.5 * (self.__sides[0] + self.__sides[1] + self.__sides[2])
        return math.sqrt((self.p - self.__sides[0]) * (self.p - self.__sides[1]) * (self.p - self.__sides[2]))

class Cube(Figure):
    sides_count = 12

    def __sides (self, __sides):
        if len(__sides) == 1:
            self.__sides = self.sides_count * [self.get_sides()]

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

