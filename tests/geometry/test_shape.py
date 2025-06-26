
from pyartkit.geometry.point import Point, P

point_a = Point(0, 0)
point_b = Point(1, 0)
point_c = Point(0, 1)
point_d = Point(1, 1)

point_e = Point(-3, 2)
point_f = Point(-3, -4)
point_g = Point(3, 2)
point_h = Point(3, -4)

point_i = Point(0, 2)
point_j = Point(2, 2)
point_k = Point(2, 0)
point_l = Point(2, -1)

def test_polygon_constructor():
    from pyartkit.geometry.shapes import Polygon


    # Test with a simple triangle
    triangle = Polygon([point_a, point_b, point_c], fill_color=None, border_color=None, border_thickness=1)
    assert triangle.get_vertices() == [point_a, point_b, point_c]

    # Test with a square
    square = Polygon([point_a, point_b, point_d, point_c], fill_color=None, border_color=None, border_thickness=1)
    assert square.get_vertices() == [point_a, point_b, point_d, point_c]

    # Test with an empty list of vertices
    empty_polygon = Polygon([], fill_color=None, border_color=None, border_thickness=1)
    assert empty_polygon.get_vertices() == []


def test_polygon_contains_point():
    from pyartkit.geometry.shapes import Polygon

    # Test with simple triangle
    triangle_i = Polygon([point_a, point_b, point_c], fill_color=None, border_color=None, border_thickness=1)
    assert triangle_i.contains(0.5, 0.5)
    assert not triangle_i.contains(1, 1)
    assert triangle_i.contains(0, 0)
    assert triangle_i.contains(0, 1)
    assert triangle_i.contains(1, 0)
    assert not triangle_i.contains(-1, 0)

    # Test with simple square
    square = Polygon([point_a, point_i, point_j, point_k], fill_color=None, border_color=None, border_thickness=1)
    assert square.contains(1, 1)
    assert square.contains(2, 2)
    assert square.contains(2, 1)
    assert square.contains(1, 2)
    assert not square.contains(2, 3)

    # Test with an empty polygon
    empty_polygon = Polygon([], fill_color=None, border_color=None, border_thickness=1)
    assert empty_polygon.contains(0, 0) is False  # Empty polygon should not contain any point

    # Test with negatives
    triangle_ii = Polygon([point_e, point_f, point_l])
    assert triangle_ii.contains(-3, -2)
    assert triangle_ii.contains(-2, 0)
    assert triangle_ii.contains(0, -1)
    assert triangle_ii.contains(2, -1)
    assert not triangle_ii.contains(2, 0)
    assert not triangle_ii.contains(1, 0)
    assert not triangle_ii.contains(-1, 1)
    assert not triangle_ii.contains(-1, -3)
    assert not triangle_ii.contains(-4, 0)

    # Test with complex polygon
    chevron = Polygon([P(-2, 0), P(-1, 0), P(0, 1), P(1, 0), P(2, 0), P(0, 2)])
    assert chevron.contains(-1, 0)
    assert chevron.contains(-1.5, 0)
    assert chevron.contains(0, 2)
    assert chevron.contains(0, 1)
    assert chevron.contains(1, 0.5)
    assert not chevron.contains(0, 0)
    assert not chevron.contains(0, 0.5)


def test_circle_constructor():
    from pyartkit.geometry.shapes import Circle

    # Test with a center point and radius
    radius = 5
    circle = Circle(point_a, radius, fill_color=None, border_color=None, border_thickness=1)
    
    assert circle._center == point_a
    assert circle._radius == radius


def test_circle_contains_point():
    from pyartkit.geometry.shapes import Circle

    # Test with a circle centered at (0, 0) with radius 5
    circle = Circle(point_a, 5, fill_color=None, border_color=None, border_thickness=1)

    assert circle.contains(0, 0)  # Center point
    assert circle.contains(3, 4)  # Point on the circle
    assert circle.contains(3, 0)  # Point inside the circle
    assert not circle.contains(6, 0)  # Point outside the circle
    assert not circle.contains(5, 5)  # Point outside the circle

    circle = Circle(point_h, 3, fill_color=None, border_color=None, border_thickness=1)
    assert circle.contains(3, -4)
    assert circle.contains(0, -4)
    assert circle.contains(2, -4)
    assert not circle.contains(0, -2)


def test_construct_rectangle():
    from pyartkit.geometry.shapes import Rectangle
    top_left = Point(1, 1)
    rectangle = Rectangle(top_left, 4, 3, fill_color=None, border_color=None, border_thickness=1)
    expected_vertices = {top_left, Point(4, 1), Point(4, -1), Point(1, -1)}
    assert len(rectangle.get_vertices()) == len(expected_vertices)
    for vertex in rectangle.get_vertices():
        for vertex_expected in expected_vertices:
            if vertex == vertex_expected:
                expected_vertices.remove(vertex_expected)
                break
    assert len(expected_vertices) == 0

def test_construct_rectangle_from_center():
    from pyartkit.geometry.shapes import Rectangle

    rectangle = Rectangle.from_center((2, 1), 5, 7, fill_color=None, border_color=None, border_thickness=1)
    expected_vertices = {Point(0, 4), Point(4, 4), Point(4, -2), Point(0, -2)}
    assert len(rectangle.get_vertices()) == len(expected_vertices)
    for vertex in rectangle.get_vertices():
        for vertex_expected in expected_vertices:
            if vertex == vertex_expected:
                expected_vertices.remove(vertex_expected)
                break
    assert len(expected_vertices) == 0

def test_construct_rectangle_from_diagonals():
    from pyartkit.geometry.shapes import Rectangle
    # TODO: Verify AI generated code
    rectangle = Rectangle.from_diagonals(P(0, 0), P(4, 3), fill_color=None, border_color=None, border_thickness=1)
    expected_vertices = {Point(0, 0), Point(4, 0), Point(4, 3), Point(0, 3)}
    assert len(rectangle.get_vertices()) == len(expected_vertices)
    for vertex in rectangle.get_vertices():
        for vertex_expected in expected_vertices:
            if vertex == vertex_expected:
                expected_vertices.remove(vertex_expected)
                break
    assert len(expected_vertices) == 0
    

def test_construct_square():
    from pyartkit.geometry.shapes import Square

    p = P(-3, 3)
    square = Square(p, 4, fill_color=None, border_color=None, border_thickness=1)
    expected_vertices = {p, Point(0, 3), Point(0, 0), Point(-3, 0)}
    assert len(square.get_vertices()) == len(expected_vertices)
    for vertex in square.get_vertices():
        for vertex_expected in expected_vertices:
            if vertex == vertex_expected:
                expected_vertices.remove(vertex_expected)
                break
    assert len(expected_vertices) == 0

def test_construct_square_from_center():
    from pyartkit.geometry.shapes import Square

    square = Square.from_center((0,0), 5, fill_color=None, border_color=None, border_thickness=1)
    expected_vertices = {Point(-2, 2), Point(-2, -2), Point(2, -2), Point(2, 2)}
    assert len(square.get_vertices()) == len(expected_vertices)
    for vertex in square.get_vertices():
        for vertex_expected in expected_vertices:
            if vertex == vertex_expected:
                expected_vertices.remove(vertex_expected)
                break
    assert len(expected_vertices) == 0