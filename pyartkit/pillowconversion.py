
from pyartkit.canvas import Canvas


def convert_canvas_to_pillow_image(canvas: Canvas):
    """
    Convert a Canvas object to a Pillow Image object.
    
    :param canvas: The Canvas object to convert.
    :return: A Pillow Image object representing the canvas.
    """
    from PIL import Image

    width = canvas.get_width()
    height = canvas.get_height()
    
    # Create a new image with the specified background color
    image = Image.new(canvas.get_color_mode(), (width, height), canvas.get_background_color().to_tuple())
    
    canvas.assign_pixel_colors()
    for pixel in canvas.get_pixels():
        color = pixel.get_color().to_tuple()
        # Set the pixel color in the image
        image.putpixel((pixel.x, pixel.y), color)

    return image


