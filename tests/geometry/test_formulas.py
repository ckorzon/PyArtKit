
def test_linear_formula():
    from pyartkit.geometry.formulas import PolynomialFormula

    # Create a linear formula
    formula = PolynomialFormula([12, 3])

    assert formula.calculate(1) == 15
    assert formula.calculate(2) == 18
    assert formula.calculate(3) == 21
    assert formula.calculate(-10) == -18
    assert formula.calculate(0) == 12


