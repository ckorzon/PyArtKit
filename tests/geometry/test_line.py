
from pyartkit.geometry.vertex import Vertex


def test_basic_line_points_crossed():
    from pyartkit.geometry.line import Line

    line = Line(Vertex(1, 2), Vertex(5, 6))

    crossed_points = line.get_points_crossed()

    expected_points = {(1,2), (2,3), (3,4), (4,5), (5,6)}

    assert len(crossed_points) == 5
    for p in expected_points:
        assert p in crossed_points, f"Expected point {p} not found in crossed points"

def test_negative_line_points_crossed():
    from pyartkit.geometry.line import Line

    line = Line(Vertex(-3, -6), Vertex(-9, -12))

    crossed_points = line.get_points_crossed()

    expected_points = {(-3,-6), (-4,-7), (-5,-8), (-6,-9), (-7,-10), (-8,-11), (-9,-12)}

    assert len(crossed_points) == 7
    
    for p in expected_points:
        assert p in crossed_points, f"Expected point {p} not found in crossed points"


def test_vertical_line_points_crossed():
    from pyartkit.geometry.line import Line

    line = Line(Vertex(2, 1), Vertex(2, 5))

    crossed_points = line.get_points_crossed()

    expected_points = {(2,1), (2,2), (2,3), (2,4), (2,5)}

    assert len(crossed_points) == 5
    for p in expected_points:
        assert p in crossed_points, f"Expected point {p} not found in crossed points"

def test_line_points_crossed_onehalf_slope():
    from pyartkit.geometry.line import Line

    line = Line(Vertex(0, 2), Vertex(4, 4))
    # Slope = 1/2

    crossed_points = line.get_points_crossed()

    expected_points = {(0,2), (1,2), (2,3), (3,4), (4, 4)}

    assert len(crossed_points) == 5
    for p in expected_points:
        assert p in crossed_points, f"Expected point {p} not found in crossed points"

def test_line_points_crossed_positive_fraction_slope():
    from pyartkit.geometry.line import Line

    line = Line(Vertex(1, 0), Vertex(4, 7))
    # Slope = 7/3

    crossed_points = line.get_points_crossed()

    expected_points = {(1,0), (2,2), (3,5), (4,7)}

    assert len(crossed_points) == 4
    for p in expected_points:
        assert p in crossed_points, f"Expected point {p} not found in crossed points"

def test_line_points_crossed_horizontal():
    from pyartkit.geometry.line import Line

    line = Line(Vertex(1, 2), Vertex(3, 2))

    crossed_points = line.get_points_crossed()

    expected_points = {(1,2), (2,2), (3,2)}

    assert len(crossed_points) == 3
    for p in expected_points:
        assert p in crossed_points, f"Expected point {p} not found in crossed points"

