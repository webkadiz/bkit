from math import pi
from .shape import Shape
from .color import Color

class Cicle(Shape):
    def __init__(self, radius, color):
        self.name = "Cicle"
        self.radius = radius
        self.color = Color(color)
    
    def area(self):
        return pi * (self.radius ** 2)

    def __repr__(self):
        return "Фигура: {}, Радиус: {}, Цвет: {}".format(
            self.getName(),
            self.radius,
            self.color
        )
