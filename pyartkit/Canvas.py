from pyartkit.color.color import COLOR_MODES, Color
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

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def get_position(self) -> tuple[int, int]:
        return self._x, self._y

    def set_color(self, color: Color):
        assert isinstance(color, Color) or color is None, "Color must be an instance of Color class."
        self._color = color

    def get_color(self) -> str:
        return self._color


class CanvasLayer:
    __slots__ = ('_graphics', '_wraparound_overlap')
    _wraparound_overlap: bool
    _graphics: list[Graphic]

    def __init__(self, wraparound_overlap: bool = False):
        """
        Initialize a new CanvasLayer with an empty list of graphics.
        wraparound_overlap: If True, the first graphic in the layer will be drawn on top of the last graphic.
        """
        self._wraparound_overlap = wraparound_overlap
        self._graphics = []

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

    def find_owning_graphic(self, x: int, y: int) -> Graphic:
        """
        Find the graphic that owns the pixel at (x, y).
        :param x: The x-coordinate of the pixel.
        :param y: The y-coordinate of the pixel.
        :return: The Graphic object that owns the pixel, or None if no graphic in this layer owns it.
        """
        is_first = True
        for graphic in self._graphics[::-1]:
            if graphic.contains(x, y):
                owner = graphic
                if is_first and self._wraparound_overlap and len(self._graphics) > 1 and self._graphics[0].contains(x, y):
                    # TODO: Eliminate redundant check for 0th graphic if wraparound_overlap is True
                    continue
                return owner
            if is_first:
                is_first = False
        return None


class Canvas:
    __slots__ = ('_layers', '_width', '_height', '_pixels', '_background_color', '_color_mode')

    _layers: list[CanvasLayer]
    _width: int
    _height: int
    _pixels: list[list[Pixel]]
    _background_color: Color
    _color_mode: str

    def __init__(self, width: int, height: int, color_mode: str, background_color: Color = None):
        self._width = width
        self._height = height
        self._layers = []
        assert color_mode in COLOR_MODES, f"Color mode must be one of {COLOR_MODES}."
        self._color_mode = color_mode
        if background_color:
            assert self._color_mode in background_color.get_supported_color_modes()
        self._background_color = background_color

    def get_background_color(self) -> Color:
        """
        Get the background color of the canvas.
        :return: The background color of the canvas.
        """
        return self._background_color

    def get_color_mode(self) -> str:
        """
        Get the color mode of the canvas.
        :return: The color mode of the canvas.
        """
        return self._color_mode

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
            owning_graphic = layer.find_owning_graphic(x, y)
            if owning_graphic:
                return owning_graphic
        return None

    def assign_pixel_colors(self):
        """
        Assign colors to pixels based on the graphics in the layers.
        This method should be called after all graphics have been added to the canvas.
        """
        self._pixels = [[Pixel(x, y, self._background_color) for x in range(self._width)] for y in range(self._height)]
        
        for row in self._pixels:
            for pixel in row:
                owner_graphic = self.find_owning_graphic(pixel.x, pixel.y)
                background_color = self._background_color 
                if owner_graphic:
                    background_color = owner_graphic.get_pixel_color(pixel.x, pixel.y)
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

    def get_pixels(self) -> list[Pixel]:
        """
        Get all pixels in the canvas.
        :return: A list of Pixel objects.
        """
        return [pixel for row in self._pixels for pixel in row]

    def get_background_color(self) -> Color:
        """
        Get the background color of the canvas.
        :return: The background color of the canvas.
        """
        return self._background_color
