

class Vertex:
    __slots__ = ("_x", "_y")
    _x: int
    _y: int

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vertex):
            return False
        return self._x == other.x and self._y == other.y
