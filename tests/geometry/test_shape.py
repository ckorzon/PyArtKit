
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


