from abc import ABC, abstractmethod


class Graphic(ABC):
    """
    Abstract base class for all graphic objects.
    """

    @abstractmethod
    def draw(self, canvas):
        """
        Draw the graphic on the given canvas.
        :param canvas: The canvas to draw on.
        """
        pass

    @abstractmethod
    def get_bounds(self):
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



    