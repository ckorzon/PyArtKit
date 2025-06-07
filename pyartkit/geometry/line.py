

from pyartkit.geometry.formulas import PolynomialFormula
from pyartkit.geometry.point import Point

DIMENSIONS = {"x", "y"}


class Line:
    __slots__ = ("_start", "_end", "_dependent_variable", "_formula", "_points_crossed")

    _start: Point
    _end: Point
    _formula: PolynomialFormula
    _points_crossed: set
    _dependent_variable: str

    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end
        self._calculate_formula()
        self._points_crossed = None

    def _calculate_formula(self):
        """Calculate the slope and intercept of the line."""
        self._dependent_variable = "y"
        if self._start.x == self._end.x:
            self._dependent_variable = "x"
            n_i = self._start.y
            n_ii = self._end.y
            f_i = self._start.x
            f_ii = self._end.x
        else:
            n_i = self._start.x
            n_ii = self._end.x
            f_i = self._start.y
            f_ii = self._end.y
        slope = (f_ii - f_i) / (n_ii - n_i)
        intercept = f_i - slope * n_i
        self._formula = PolynomialFormula([intercept, slope])

    def __str__(self):
        return f"Line[{self._start}, {self._end}]"

    def get_points_crossed(self):
        """Return the points crossed by the line."""
        if not self._points_crossed or len(self._points_crossed) == 0:
            self._points_crossed = set()
            # Determine line direction
            step = 1
            if (self._dependent_variable == "y" and self._start.x > self._end.x) or (self._dependent_variable == "x" and self._start.y > self._end.y):
                step = -1
            # Calculate points crossed based on the dependent variable
            if self._dependent_variable == "y":
                for x in range(self._start.x, self._end.x + step, step):
                    self._points_crossed.add((x, round(self._formula.calculate(x))))
            else:
                for y in range(self._start.y, self._end.y + step, step):
                    self._points_crossed.add((round(self._formula.calculate(y)), y))
        return self._points_crossed

