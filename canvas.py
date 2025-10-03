import numpy as np
from PIL import Image


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
