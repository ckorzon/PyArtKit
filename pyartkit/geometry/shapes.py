from abc import ABC, abstractmethod


# * NOTE: PIL has a built-in ImageDraw class that can be used to draw shapes on images. BUT it doesn't support gradients or edge colors. Should we extend it or create our own?

class Shape(ABC):

    def __init__(self, fill_color=None, edge_color=None, edge_width=1):
        self._fill_color = fill_color
        self._edge_color = edge_color
        self._edge_width = edge_width

    def set_fill_color(self, color):
        """Set the fill color of the shape."""
        self._fill_color = color

    def get_fill_color(self):
        """Get the fill color of the shape."""
        return self._fill_color

    def set_edge_color(self, color):
        """Set the edge color of the shape."""
        self._edge_color = color

    def get_edge_color(self):
        """Get the edge color of the shape."""
        return self._edge_color

    def set_edge_width(self, width):
        """Set the edge width of the shape."""
        self._edge_width = width

    def get_edge_width(self):
        """Get the edge width of the shape."""
        return self._edge_width


    # TODO
    # We don't really care about area or perimeter for making art. Focus on fill color, perimiter color, and edge width.
    # Also consider colors for vertices. A method to get the set of points in the shape would be useful, or a method to check if a point is in the shape.
    # Will eventually need layers applied to shapes.
    pass