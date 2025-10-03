from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def draw(self, canvas):
        """Draw the figure"""
        pass


class Square(Figure):
    """
    This class represents a square object
    """
    def __init__(self, x, y, side, color):
        super().__init__(x, y, color)
        self.side = side

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.side, self.y:self.y + self.side] = self.color


class Rectangle(Figure):
    """
    This class represents a rectangle object
    """
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.height, self.y: self.y + self.width] = self.color
