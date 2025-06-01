

def make_gradient_rgb(start_color, end_color, steps):
    """
    Create a gradient between two colors.

    Args:
        start_color (tuple): The starting color as an RGB tuple.
        end_color (tuple): The ending color as an RGB tuple.
        steps (int): The number of steps in the gradient.

    Returns:
        list: A list of RGB tuples representing the gradient.
    """
    assert len(start_color) == len(end_color) and len(start_color) in [3, 4], "Colors must be RGB or RGBA tuples"
    gradient = []
    for step in range(steps):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * step / (steps - 1))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * step / (steps - 1))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * step / (steps - 1))
        if len(start_color) == 4:
            a = int(start_color[3] + (end_color[3] - start_color[3]) * step / (steps - 1))
            gradient.append((r, g, b, a))
        else:
            gradient.append((r, g, b))
    return gradient

