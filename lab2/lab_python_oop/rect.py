from .shape import Shape
from .color import Color

class Rect(Shape):
    def __init__(self, width, height, color):
        self.name = "Rect"
        self.width = width
        self.height = height
        self.color = Color(color)
    
    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Фигура: {}, Ширина: {}, Высота: {}, Цвет: {}".format(
            self.getName(),
            self.width,
            self.height,
            self.color
        )
