from .rect import Rect

class Square(Rect):
    def __init__(self, side, color):
        super().__init__(side, side, color)
        self.name = "Square"
