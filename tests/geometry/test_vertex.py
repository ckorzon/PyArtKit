from pyartkit.geometry.vertex import Vertex

def test_vertex():
    # Create a vertex
    v = Vertex(7, 24)

    # Test the coordinates
    assert v.x == 7
    assert v.y == 24

def test_vertex_equality():
    v = Vertex(1, 2)

    # Test the equality operator
    v2 = Vertex(1, 2)
    assert v == v2

    # Test the inequality operator
    v3 = Vertex(4, 5)
    assert v != v3

