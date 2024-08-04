class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides) if len(sides) == self.sides_count else [1] * self.sides_count
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print(f"Cannot set color to ({r}, {g}, {b})")

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print(f"Cannot set sides to {new_sides}")

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        if self.get_sides():
            return self.get_sides()[0] / (2 * 3.14159)
        return 0

    def get_square(self):
        return 3.14159 * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        if len(self.get_sides()) == 3:
            a, b, c = self.get_sides()
            s = sum(self.get_sides()) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            return 2 * area / a
        return 0

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            super().__init__(color, *([sides[0]] * self.sides_count))
        else:
            super().__init__(color, *sides)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)
print(circle1.get_color())  # Изменится
cube1.set_color(300, 70, 15)
print(cube1.get_color())  # Не изменится


cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())


print(len(circle1))


print(cube1.get_volume())