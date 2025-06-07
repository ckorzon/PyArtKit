from pyartkit.geometry.point import Point

def test_point():
    # Create a vertex
    v = Point(7, 24)

    # Test the coordinates
    assert v.x == 7
    assert v.y == 24

def test_point_equality():
    v = Point(1, 2)

    # Test the equality operator
    v2 = Point(1, 2)
    assert v == v2

    # Test the inequality operator
    v3 = Point(4, 5)
    assert v != v3

