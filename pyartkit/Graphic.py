from abc import ABC, abstractmethod

from pyartkit.color.color import Color


class Graphic(ABC):
    """
    Abstract base class for all graphic objects.
    """


    @abstractmethod
    def get_bounds(self) -> tuple:
        """
        Get the bounding box of the graphic.
        :return: A tuple (x_min, y_min, x_max, y_max).
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Check if the graphic is empty.
        :return: True if the graphic is empty, False otherwise.
        """
        pass

    @abstractmethod
    def set_center(self, x, y):
        """
        Set the center of the graphic.
        :param x: The x-coordinate of the center.
        :param y: The y-coordinate of the center.
        """
        pass

    @abstractmethod
    def get_center(self) -> tuple:
        """
        Get the center of the graphic.
        :return: A tuple (x, y) representing the center coordinates.
        """
        pass


    # * Does this work for lines? 2D elements?
    @abstractmethod
    def set_top_left(self, x, y):
        """
        Set the top-left corner of the graphic.
        :param x: The x-coordinate of the top-left corner.
        :param y: The y-coordinate of the top-left corner.
        """
        pass

    @abstractmethod
    def contains(self, x: int, y: int) -> bool:
        """
        Check if the graphic contains a point.
        :param x: The x-coordinate of the point.
        :param y: The y-coordinate of the point.
        :return: True if the graphic contains the point, False otherwise.
        """
        pass

    @abstractmethod
    def get_pixel_color(self, x: int = None, y: int = None) -> Color:
        """
        Get the color of the graphic.
        :param x: The x-coordinate of the point (optional).
        :param y: The y-coordinate of the point (optional).
        :return: A tuple representing the color (R, G, B, A).
        """
        pass
