from pyartkit.graphic import Graphic


class CanvasLayer:
    __slots__ = ('_graphics', '_canvas')

    _graphics: list[Graphic]

    def add_graphic(self, graphic: Graphic, slot: int = -1):
        """
        Add a graphic to the layer with a specified priority.
        :param graphic: The graphic to add.
        :param slot: The slot into which to insert the graphic in this layer's queue (default is -1).
        """
        self._graphics.insert(slot, graphic)

    def add_graphic_first(self, graphic: Graphic):
        """
        Add a graphic to the front of the layer's queue.
        :param graphic: The graphic to add.
        """
        self.add_graphic(graphic, 0)

    def add_graphic_last(self, graphic: Graphic):
        """
        Add a graphic to the end of the layer's queue.
        :param graphic: The graphic to add.
        """
        self.add_graphic(graphic, -1)


class Canvas:
    __slots__ = ('_layers', '_width', '_height')

    _layers: list[CanvasLayer]
    _width: int
    _height: int

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._layers = []

    def add_layer(self, layer: CanvasLayer):
        """
        Add a layer to the canvas.
        :param layer: The layer to add.
        """
        self._layers.append(layer)
