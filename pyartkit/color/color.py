
from abc import ABC


class Color(ABC):
    """Base class for all Color types."""
    pass


class RGBColor(Color):
    """
    A class representing an RGB color.
    
    Attributes:
        r (int): Red component (0-255).
        g (int): Green component (0-255).
        b (int): Blue component (0-255).
    """

    __slots__ = ('r', 'g', 'b')
    
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def to_tuple(self) -> tuple:
        """
        Convert the RGB color to a tuple.
        
        Returns:
            tuple: An RGB tuple (r, g, b).
        """
        return (self.r, self.g, self.b)

    @staticmethod
    def from_tuple(color_tuple: tuple) -> 'RGBColor':
        """
        Create an RGBColor instance from a tuple.
        
        Args:
            color_tuple (tuple): An RGB tuple (r, g, b).
        
        Returns:
            RGBColor: An instance of RGBColor.
        """
        if len(color_tuple) != 3:
            raise ValueError("Tuple must have exactly three elements (r, g, b).")
        return RGBColor(*color_tuple)

    def __str__(self):
        """
        String representation of the RGB color.
        
        Returns:
            str: A string in the format 'RGB(r, g, b)'.
        """
        return f"RGB({self.r}, {self.g}, {self.b})"


class RGBAColor(RGBColor):
    """
    A class representing an RGBA color, which extends RGBColor.
    
    Attributes:
        r (int): Red component (0-255).
        g (int): Green component (0-255).
        b (int): Blue component (0-255).
        a (int): Alpha component (0-255).
    """

    __slots__ = ('a',)

    def __init__(self, r: int, g: int, b: int, a: int):
        super().__init__(r, g, b)
        self.a = a

    def to_tuple(self) -> tuple:
        """
        Convert the RGBA color to a tuple.
        
        Returns:
            tuple: An RGBA tuple (r, g, b, a).
        """
        return (self.r, self.g, self.b, self.a)

    @staticmethod
    def from_tuple(color_tuple: tuple) -> 'RGBAColor':
        """
        Create an RGBAColor instance from a tuple.
        
        Args:
            color_tuple (tuple): An RGBA tuple (r, g, b, a).
        
        Returns:
            RGBAColor: An instance of RGBAColor.
        """
        if len(color_tuple) != 4:
            raise ValueError("Tuple must have exactly four elements (r, g, b, a).")
        return RGBAColor(*color_tuple)

    def __str__(self):
        """
        String representation of the RGBA color.
        
        Returns:
            str: A string in the format 'RGBA(r, g, b, a)'.
        """
        return f"RGBA({self.r}, {self.g}, {self.b}, {self.a})"