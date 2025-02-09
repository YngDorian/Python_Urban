import math

class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = []
        self.__color = []
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Некорректные значения цвета. Цвет остался прежним.")

    def __is_valid_sides(self):
        return all(isinstance(side, int) and side > 0 for side in self.__sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return len(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            print(f"Количество новых сторон ({len(new_sides)}) должно равняться {self.sides_count}. Изменение не прошло.")
            return
        if all(isinstance(side, int) and side > 0 for side in new_sides):
            self.__sides = list(new_sides)
            print(f"Стороны изменены на: {self.__sides}")
        else:
            print("Некорректные данные для сторон. Изменения не внесены.")

class Circle(Figure):
    sides_count = 1

    def __init__(self, circumference):
        super().__init__()
        self.__radius = circumference / (2 * math.pi)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, a, b, c):
        super().__init__()
        self.set_sides(a, b, c)
        self.__a = a
        self.__b = b
        self.__c = c

    def get_square(self):
        s = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, side):
        super().__init__()
        self.set_sides(*([side] * self.sides_count))
        self.__side = side

    def get_volume(self):
        return self.__side ** 3

if __name__ == "__main__":
    circle = Circle(31.4)
    print("Radius of circle:", circle.get_radius())
    print("Area of circle:", circle.get_square())

    triangle = Triangle(3, 4, 5)
    print("Area of triangle:", triangle.get_square())

    cube = Cube(3)
    print("Volume of cube:", cube.get_volume())
