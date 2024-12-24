import math

class Figure:
    def __init__(self, color, *sides):
        self._sides = list(sides) if self._is_valid_sides(*sides) else [1] * self.sides_count
        self._color = list(color)
        self.filled = False  

    @property
    def sides_count(self):
        return 0

    def get_color(self):
        return self._color

    def _is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in [r, g, b])

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self._color = [r, g, b]

    def _is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, (int, float)) and side > 0 for side in new_sides)

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self._sides = list(new_sides)

class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self._radius = self._sides[0] / 2 if self.sides_count == 1 else 1

    @property
    def sides_count(self):
        return 1

    def get_square(self):
        return math.pi * (self._radius ** 2)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        if self.sides_count == 1:
            self._radius = self._sides[0] / 2

class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    @property
    def sides_count(self):
        return 3

    def get_square(self):
        s = sum(self._sides) / 2
        if all(side < s for side in self._sides):
            return math.sqrt(s * (s - self._sides[0]) * (s - self._sides[1]) * (s - self._sides[2]))
        return 0

class Cube(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    @property
    def sides_count(self):
        return 12

    def _sides_count_array(self, side_length):
        return [side_length] * self.sides_count

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self._sides = self._sides_count_array(new_sides[0])
        else:
            self._sides = [1] * self.sides_count

    def get_volume(self):
        return self._sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())


cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())


print(len(circle1))


print(cube1.get_volume())