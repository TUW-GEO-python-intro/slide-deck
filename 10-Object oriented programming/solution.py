import numpy as np


class Shape(object):
    num = 0

    def __init__(self, color):
        self.color = color
        Shape.num += 1

    @staticmethod
    def how_many():
        return Shape.num


class Rectangle(Shape):

    def __init__(self, width, height, color):
        super(Rectangle, self).__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, radius, color):
        super(Circle, self).__init__(color)
        self.radius = radius

    def calculate_area(self):
        return np.pi * self.radius ** 2

rect1 = Rectangle(10, 10, 'white')
circ1 = Circle(2, 'blue')

print(rect1.calculate_area())
print(circ1.calculate_area())
print(Shape.how_many())
