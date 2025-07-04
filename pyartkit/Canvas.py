from pyartkit.color.color import Color
from pyartkit.graphic import Graphic

class Pixel:
    __slots__ = ('_x', '_y', '_color')

    _x: int
    _y: int
    _color: Color

    def __init__(self, x: int, y: int, color: Color):
        self._x = x
        self._y = y
        self._color = color

    def get_position(self) -> tuple[int, int]:
        return self._x, self._y

    def set_color(self, color: Color):
        assert isinstance(color, Color) or color is None, "Color must be an instance of Color class."
        self._color = color

    def get_color(self) -> str:
        return self._color


class CanvasLayer:
    __slots__ = ('_graphics')

    _graphics: list[Graphic]

    def add_graphic(self, graphic: Graphic, priority: int = -1):
        """
        Add a graphic to the layer with a specified priority.
        :param graphic: The graphic to add.
        :param slot: The slot into which to insert the graphic in this layer's queue (default is -1).
        """
        if priority < 0 or priority >= len(self._graphics):
            self._graphics.append(graphic)
            return
        if priority == 0:
            self._graphics = [graphic] + self._graphics
            return
        self._graphics.insert(priority, graphic)

    def add_graphic_front(self, graphic: Graphic):
        """
        Add a graphic to the front of the layer's queue.
        :param graphic: The graphic to add.
        """
        self.add_graphic(graphic, -1)

    def add_graphic_back(self, graphic: Graphic):
        """
        Add a graphic to the end of the layer's queue.
        :param graphic: The graphic to add.
        """
        self.add_graphic(graphic, 0)

    def get_graphics(self) -> list[Graphic]:
        """
        Get the list of graphics in this layer.
        :return: A list of Graphic objects.
        """
        return self._graphics


class Canvas:
    __slots__ = ('_layers', '_width', '_height')

    _layers: list[CanvasLayer]
    _width: int
    _height: int
    _pixels: list[list[Pixel]]
    _background_color: Color

    def __init__(self, width: int, height: int, background_color: Color = None):
        self._width = width
        self._height = height
        self._layers = []
        self._background_color

    def add_layer(self, layer: CanvasLayer, priority: int = -1):
        """
        Add a layer to the canvas.
        :param layer: The layer to add.
        """
        if priority < 0 or priority >= len(self._layers):
            self._layers.append(layer)
        else:
            self._layers.insert(priority, layer)

    def get_width(self) -> int:
        """
        Get the width of the canvas.
        :return: The width of the canvas.
        """
        return self._width
    
    def get_height(self) -> int:
        """
        Get the height of the canvas.
        :return: The height of the canvas.
        """
        return self._height

    def find_owning_graphic(self, x: int, y: int) -> Graphic:
        """
        Find the graphic that owns the pixel at (x, y).
        :param x: The x-coordinate of the pixel.
        :param y: The y-coordinate of the pixel.
        :return: The Graphic object that owns the pixel, or None if no graphic owns it.
        """
        for layer in self._layers[::-1]:
            for graphic in layer.get_graphics()[::-1]:
                if graphic.contains(x, y):
                    return graphic
        return None

    def assign_pixel_colors(self):
        """
        Assign colors to pixels based on the graphics in the layers.
        This method should be called after all graphics have been added to the canvas.
        """
        self._pixels = [[Pixel(x, y, self._background_color) for x in range(self._width)] for y in range(self._height)]
        
        for row in self._pixels:
            for pixel in row:
                owner_graphic = self.find_owning_graphic(pixel._x, pixel._y)
                background_color = self._background_color 
                if owner_graphic:
                    background_color = owner_graphic.get_pixel_color()
                pixel.set_color(background_color)

    def get_pixel(self, x: int, y: int) -> Pixel:
        """
        Get the pixel at (x, y).
        :param x: The x-coordinate of the pixel.
        :param y: The y-coordinate of the pixel.
        :return: The Pixel object at (x, y).
        """
        if 0 <= x < self._width and 0 <= y < self._height:
            return self._pixels[y][x]
        raise IndexError("Pixel coordinates out of bounds.")

    def get_background_color(self) -> Color:
        """
        Get the background color of the canvas.
        :return: The background color of the canvas.
        """
        return self._background_color
