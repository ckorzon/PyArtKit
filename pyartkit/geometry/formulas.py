


class PolynomialFormula:
    """Class to represent a mathematical formula for a line or polynomial. Requires exactly 1 dependent variable and 1 independent variable."""

    __slots__ = ('_coefficients')

    def __init__(self, coefficients: list):
        self._coefficients = coefficients
        assert len(coefficients) >= 1, "Must have at least one coefficient"
        for a in coefficients:
            assert isinstance(a, (int, float)), "Coefficients must be int or float"

    def calculate(self, independent_value: float) -> float:
        """Calculate the dependent variable given the independent variable."""
        result = 0
        for i, coefficient in enumerate(self._coefficients):
            result += coefficient * (independent_value ** i)
        return result

    @property
    def degree(self) -> int:
        """Return the degree of the polynomial."""
        return len(self._coefficients) - 1

