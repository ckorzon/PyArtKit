from abc import abstractmethod
from typing import List

from pyartkit.color.color import Color
from pyartkit.color.colorscheme import ColorScheme
from pyartkit.geometry.point import Point
from pyartkit.graphic import Graphic


# * NOTE: PIL has a built-in ImageDraw class that can be used to draw shapes on images. BUT it doesn't support gradients or edge colors. Should we extend it or create our own?

class Shape(Graphic):

    __slots__ = ('_fill_color', '_border_color', '_border_thickness')
    _fill_color: ColorScheme
    _border_color: ColorScheme
    _border_thickness: int


    def __init__(self, fill_color: ColorScheme = None, border_color: ColorScheme = None, border_thickness=1):
        self._fill_color = fill_color
        self._border_color = border_color
        assert isinstance(border_thickness, int) and border_thickness >= 0, "Border thickness must be a non-negative integer."
        self._border_thickness = border_thickness

    def set_fill_color_scheme(self, color):
        """Set the fill color of the shape."""
        self._fill_color = color

    def get_fill_color_scheme(self):
        """Get the fill color of the shape."""
        return self._fill_color

    def set_border_color_scheme(self, color):
        """Set the edge color of the shape."""
        self._border_color = color

    def get_border_color_scheme(self):
        """Get the edge color of the shape."""
        return self._border_color

    def set_border_thickness(self, width):
        """Set the edge width of the shape."""
        self._border_thickness = width

    def get_border_thickness(self):
        """Get the edge width of the shape."""
        return self._border_thickness

    def get_pixel_color(self, x: int = None, y: int = None) -> Color:
        """
        Get the color of the shape at a specific pixel.
        
        Args:
            x (int): The x-coordinate of the pixel.
            y (int): The y-coordinate of the pixel.
        
        Returns:
            Color: The color of the shape at the specified pixel.
        """
        # TODO: Determine if the pixel is part of the border or fill
        return self._fill_color.get_color_for_pixel(x, y) if self._fill_color else None

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

    def get_bounds(self) -> tuple:
        min_x, min_y, max_x, max_y = None, None, None, None
        for v in self._vertices:
            if min_x is None or v.x < min_x:
                min_x = v.x
            if max_x is None or v.x > max_x:
                max_x = v.x
            if min_y is None or v.y < min_y:
                min_y = v.y
            if max_y is None or v.y > max_y:
                max_y = v.y
        return (min_x, min_y, max_x, max_y)

    def is_empty(self) -> bool:
        """
        Check if the polygon is empty (i.e., has no vertices).
        
        Returns:
            bool: True if the polygon is empty, False otherwise.
        """
        return len(self._vertices) == 0

    def get_center(self) -> tuple:
        """Return the center of the polygon as a tuple (x, y)."""
        if self.is_empty():
            return (0, 0)
        min_x, min_y, max_x, max_y = self.get_bounds()
        x_bounds = (min_x, max_x)
        y_bounds = (min_y, max_y)
        width = x_bounds[1] - x_bounds[0]
        height = y_bounds[1] - y_bounds[0]
        center_x = x_bounds[0] + width // 2
        center_y = y_bounds[0] + height // 2
        return center_x, center_y

    def set_center(self, x, y):
        center: tuple = self.get_center()
        delta_x = x - center[0]
        delta_y = y - center[1]
        for vertex in self._vertices:
            vertex.translate(delta_x, delta_y)

    def set_top_left(self, x: int, y: int):
        """
        Set the top-left corner of the polygon to the specified coordinates.
        
        Args:
            x (int): The x-coordinate of the top-left corner.
            y (int): The y-coordinate of the top-left corner.
        """
        min_x, _, _, max_y = self.get_bounds()
        delta_x = x - min_x
        delta_y = y - max_y
        for vertex in self._vertices:
            vertex.translate(delta_x, delta_y)

    def get_vertices(self) -> List[Point]:
        """
        Get the vertices of the polygon.
        
        Returns:
            List[Point]: The list of vertices.
        """
        return self._vertices


class Rectangle(Polygon):

    def __init__(self, top_left: Point, width: int, height: int, fill_color: ColorScheme = None, border_color: ColorScheme = None, border_thickness=1):
        """
        Initialize a rectangle with the top-left corner, width, height, and optional colors.
        
        Args:
            top_left (Point): The top-left corner of the rectangle.
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            fill_color (ColorScheme, optional): The fill color of the rectangle. Defaults to None.
            border_color (ColorScheme, optional): The border color of the rectangle. Defaults to None.
            border_thickness (int, optional): The border thickness of the rectangle. Defaults to 1.
        """
        # Count the initial vertex as 1 width since we are operating on pixels
        width_delta = max(0, width - 1)
        height_delta = max(0, height - 1)
        vertices = [
            top_left,
            Point(top_left.x + width_delta, top_left.y),
            Point(top_left.x + width_delta, top_left.y - height_delta),
            Point(top_left.x, top_left.y - height_delta)
        ]
        super().__init__(vertices, fill_color, border_color, border_thickness)

    @staticmethod
    def from_diagonals(corner_a: Point, corner_b: Point, fill_color: ColorScheme = None, border_color: ColorScheme = None, border_thickness=1) -> 'Rectangle':
        """
        Create a rectangle from the top-left and bottom-right corners.
        
        Args:
            corner_a (Point): One corner of the rectangle.
            corner_b (Point): A corner of the rectangle diagonal from corner_a.
            fill_color (ColorScheme, optional): The fill color of the rectangle. Defaults to None.
            border_color (ColorScheme, optional): The border color of the rectangle. Defaults to None.
            border_thickness (int, optional): The border thickness of the rectangle. Defaults to 1.
        
        Returns:
            Rectangle: A new Rectangle instance.
        """
        width = abs(corner_a.x - corner_b.x) + 1
        height = abs(corner_a.y - corner_b.y) + 1
        top_left = Point(min(corner_a.x, corner_b.x), max(corner_a.y, corner_b.y))
        return Rectangle(top_left, width, height, fill_color, border_color, border_thickness)

    @staticmethod
    def from_center(center: tuple, width: int, height: int, fill_color: ColorScheme = None, border_color: ColorScheme = None, border_thickness=1) -> 'Rectangle':
        """
        Create a rectangle from the center point, width, and height.
        
        Args:
            center (tuple): The center point of the rectangle as (x, y).
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            fill_color (ColorScheme, optional): The fill color of the rectangle. Defaults to None.
            border_color (ColorScheme, optional): The border color of the rectangle. Defaults to None.
            border_thickness (int, optional): The border thickness of the rectangle. Defaults to 1.
        
        Returns:
            Rectangle: A new Rectangle instance.
        """
        top_left = Point(center[0] - width // 2, center[1] + height // 2)
        return Rectangle(top_left, width, height, fill_color, border_color, border_thickness)


class Square(Rectangle):
    def __init__(self, top_left: Point, side_length: int, fill_color: ColorScheme = None, border_color: ColorScheme = None, border_thickness = 1):
        """
        Initialize a square with the top-left corner and side length.
        
        Args:
            top_left (Point): The top-left corner of the square.
            side_length (int): The length of each side of the square.
            fill_color (ColorScheme, optional): The fill color of the square. Defaults to None.
            border_color (ColorScheme, optional): The border color of the square. Defaults to None.
            border_thickness (int, optional): The border thickness of the square. Defaults to 1.
        """
        super().__init__(top_left, side_length, side_length, fill_color, border_color, border_thickness)

    @staticmethod
    def from_diagonals(corner_a: Point, corner_b: Point, fill_color: ColorScheme = None, border_color: ColorScheme = None, border_thickness = 1):
        width = abs(corner_b.x - corner_a.x)
        height = abs(corner_b.y - corner_a.y)
        assert width == height, "For a square, the width and height must be equal."
        top_left = Point(min(corner_a.x, corner_b.x), min(corner_a.y, corner_b.y))
        return Square(top_left, width, fill_color, border_color, border_thickness)
 
    @staticmethod
    def from_center(center: tuple, side_length: int, fill_color: ColorScheme = None, border_color: ColorScheme = None, border_thickness=1) -> 'Square':
        """
        Create a square from the center point and side length.
        
        Args:
            center (tuple): The center point of the square as (x, y).
            side_length (int): The length of each side of the square.
            fill_color (ColorScheme, optional): The fill color of the square. Defaults to None.
            border_color (ColorScheme, optional): The border color of the square. Defaults to None.
            border_thickness (int, optional): The border thickness of the square. Defaults to 1.
        
        Returns:
            Square: A new Square instance.
        """
        top_left = Point(center[0] - side_length // 2, center[1] + side_length // 2)
        return Square(top_left, side_length, fill_color, border_color, border_thickness)


class Circle(Shape):

    __slots__ = ('_center', '_radius', '_fill_color', '_border_color', '_border_thickness')
    _center: Point
    _radius: int

    def __init__(self, center: Point, radius: int, fill_color: ColorScheme = None, border_color: ColorScheme = None, border_thickness=1):
        super().__init__(fill_color, border_color, border_thickness)
        self._center = center
        self._radius = radius

    def get_bounds(self):
        if not self._center or self._radius <= 0:
            return (None, None, None, None)
        return (
            self._center.x - self._radius,
            self._center.y - self._radius,
            self._center.x + self._radius,
            self._center.y + self._radius
        )

    def get_center(self) -> tuple:
        return self._center.x, self._center.y

    def set_center(self, x: int, y: int):
        """
        Set the center of the circle to the specified coordinates.
        
        Args:
            x (int): The x-coordinate of the new center.
            y (int): The y-coordinate of the new center.
        """
        self._center = Point(x, y)

    def is_empty(self):
        return not self._center or self._radius <= 0

    def set_top_left(self, x, y):
        current_top_left = (self.min_x(), self.max_y())
        delta_x = x - current_top_left[0]
        delta_y = y - current_top_left[1]
        self._center.x += delta_x
        self._center.y -= delta_y

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
