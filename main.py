from abc import ABC, abstractmethod
from  PIL import Image
import numpy as np

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

class Canvas:
    """
    This class represents a canvas object
    """

    def __init__(self, height, width, color, canvas_path):
        self.height = height
        self.width = width
        self.color = color # Ej: [255, 255, 0]
        self.canvas_path = canvas_path
        self.data = self._generate_canvas()

    def _generate_canvas(self):
        data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        data[:] = self.color
        return data

    def save(self):
        image = Image.fromarray(self.data, 'RGB')
        image.save(self.canvas_path)

canvas1 = Canvas(height=10, width=10, color=(0,0,0), canvas_path='assets/canvas1.png')
rectangle1 = Rectangle(x=1, y=1, width=3, height=2, color=(255,0,0))
rectangle1.draw(canvas1)
square1 = Square(x=1, y=4, side=2, color=(0,0,255))
square1.draw(canvas1)
canvas1.save()



