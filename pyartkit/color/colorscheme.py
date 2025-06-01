from abc import ABC, abstractmethod

from pyartkit.color.color import Color

class ColorScheme(ABC):
    # TODO
    pass

    @abstractmethod
    def get_color_for_pixel(self, x, y) -> Color:
        """
        Get the color for a pixel at (x, y) coordinates.
        
        Args:
            x (int): The x-coordinate of the pixel.
            y (int): The y-coordinate of the pixel.
        
        Returns:
            tuple: An RGB or RGBA color tuple.
        """
        pass

class StaticColorScheme(ABC, ColorScheme):
    """
    A static color scheme that returns a fixed color for all pixels.
    """

    def __init__(self, color: Color):
        """
        Initialize the static color scheme with a fixed color.
        
        Args:
            color (tuple): An RGB or RGBA color tuple.
        """
        self.color = color

    def get_color_for_pixel(self, x, y) -> Color:
        return self.color