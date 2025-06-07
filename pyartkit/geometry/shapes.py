from abc import ABC, abstractmethod
from typing import List

from pyartkit.color.colorscheme import ColorScheme
from pyartkit.geometry.point import Point


# * NOTE: PIL has a built-in ImageDraw class that can be used to draw shapes on images. BUT it doesn't support gradients or edge colors. Should we extend it or create our own?

class Shape(ABC):

    __slots__ = ('_fill_color', '_border_color', '_border_thickness')
    _fill_color: ColorScheme
    _border_color: ColorScheme
    _border_thickness: int


    def __init__(self, fill_color: ColorScheme = None, border_color: ColorScheme = None, border_thickness=1):
        self._fill_color = fill_color
        self._border_color = border_color
        assert isinstance(border_thickness, int) and border_thickness >= 0, "Border thickness must be a non-negative integer."
        self._border_thickness = border_thickness

    def set_fill_color(self, color):
        """Set the fill color of the shape."""
        self._fill_color = color

    def get_fill_color(self):
        """Get the fill color of the shape."""
        return self._fill_color

    def set_border_color(self, color):
        """Set the edge color of the shape."""
        self._border_color = color

    def get_border_color(self):
        """Get the edge color of the shape."""
        return self._border_color

    def set_border_thickness(self, width):
        """Set the edge width of the shape."""
        self._border_thickness = width

    def get_border_thickness(self):
        """Get the edge width of the shape."""
        return self._border_thickness

    @abstractmethod
    def contains(self, x: int, y: int) -> bool:
        """
        Check if the shape contains the point (x, y).
        
        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.
        
        Returns:
            bool: True if the shape contains the point, False otherwise.
        """
        pass

    @abstractmethod
    def max_x(self) -> int:
        """
        Get the maximum x-coordinate of the shape.
        
        Returns:
            int: The maximum x-coordinate.
        """
        pass

    @abstractmethod
    def max_y(self) -> int:
        """
        Get the maximum y-coordinate of the shape.
        
        Returns:
            int: The maximum y-coordinate.
        """
        pass

    @abstractmethod
    def min_x(self) -> int:
        """
        Get the minimum x-coordinate of the shape.
        
        Returns:
            int: The minimum x-coordinate.
        """
        pass

    @abstractmethod
    def min_y(self) -> int:
        """
        Get the minimum y-coordinate of the shape.
        
        Returns:
            int: The minimum y-coordinate.
        """
        pass


class Polygon(Shape):
    """
    A polygon shape defined by a list of vertices.
    """

    __slots__ = ('_vertices', '_fill_color', '_border_color', '_border_thickness')
    _vertices: List[Point]
    _fill_color: ColorScheme
    _border_color: ColorScheme
    _border_thickness: int

    def __init__(self, vertices: List[Point], fill_color: ColorScheme = None, border_color: ColorScheme = None, border_thickness=1):
        super().__init__(fill_color, border_color, border_thickness)
        self._vertices = vertices

    def contains(self, x: int, y: int) -> bool:
        contains_point = False
        if not len(self._vertices) > 2:
            return contains_point
        vertex_b = self._vertices[-1]
        for vertex_a in self._vertices:
            if x == vertex_a.x and y == vertex_a.y:
                return True
            # * Adapt the algorithm to include points on the horizontal edges
            point_on_horizontal_edge = vertex_a.y == y and vertex_b.y == y
            if point_on_horizontal_edge:
                if (x <= vertex_a.x) != (x <= vertex_b.x):
                    return True

            # * Standard case for point within bounds
            point_within_y_bounds = (vertex_a.y > y) != (vertex_b.y > y)
            # Skip if the point is not within the y bounds of the current edge to avoid division by zero
            if not point_within_y_bounds:
                vertex_b = vertex_a
                continue
            x_intersection = (vertex_b.x - vertex_a.x) * (y - vertex_a.y) / (vertex_b.y - vertex_a.y) + vertex_a.x
            if x == x_intersection:
                return True
            if x < x_intersection:
                contains_point = not contains_point
            vertex_b = vertex_a
        return contains_point

    def max_x(self) -> int:
        return max(vertex.x for vertex in self.vertices)

    def max_y(self) -> int:
        return max(vertex.y for vertex in self.vertices)

    def min_x(self) -> int:
        return min(vertex.x for vertex in self.vertices)

    def min_y(self) -> int:
        return min(vertex.y for vertex in self.vertices)

    def get_vertices(self) -> List[Point]:
        """
        Get the vertices of the polygon.
        
        Returns:
            List[Point]: The list of vertices.
        """
        return self._vertices


class Rectangle(Polygon):
    # TODO
    pass


class Circle(Shape):

    __slots__ = ('_center', '_radius', '_fill_color', '_border_color', '_border_thickness')
    _center: Point
    _radius: int

    def __init__(self, center: Point, radius: int, fill_color: ColorScheme = None, border_color: ColorScheme = None, border_thickness=1):
        super().__init__(fill_color, border_color, border_thickness)
        self._center = center
        self._radius = radius

    def contains(self, x: int, y: int) -> bool:
        return (x - self._center.x) ** 2 + (y - self._center.y) ** 2 <= self._radius ** 2

    def max_x(self) -> int:
        return self._center.x + self._radius

    def max_y(self) -> int:
        return self._center.y + self._radius

    def min_x(self) -> int:
        return self._center.x - self._radius

    def min_y(self) -> int:
        return self._center.y - self._radius
