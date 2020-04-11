"""

Copyright (c) 2016-2020 Vanessa Sochat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from PIL import Image

"""Credit goes to https://www.hackerearth.com/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
The one modification I added was to scale the new_width by 2, because text characters tend to be thinner than they
are wide, and the current method produced images that were (generally) too tall!
"""
ASCII_CHARS = ["#", "?", "%", ".", "S", "+", ".", "*", ":", ",", "@"]


def scale_image(image, new_width):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)
    # This scales it wider than tall, since characters are biased
    new_image = image.resize((new_width * 2, new_height))
    return new_image


def convert_to_grayscale(image):
    return image.convert("L")


def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.
    0-255 is divided into 11 ranges of 25 pixels each.
    """
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [
        ASCII_CHARS[pixel_value // range_width] for pixel_value in pixels_in_image
    ]
    return "".join(pixels_to_chars)


def convert_image_to_ascii(image, new_width):
    image = scale_image(image, new_width)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [
        pixels_to_chars[index : index + new_width * 2]
        for index in range(0, len_pixels_to_chars, new_width * 2)
    ]
    return "\n".join(image_ascii)


def handle_image_conversion(image_filepath, new_width=100):
    image = None
    try:
        image = Image.open(image_filepath)
    except:
        print(
            "Unable to open image file {image_filepath}.".format(
                image_filepath=image_filepath
            )
        )
        print(e)
        return
    image_ascii = convert_image_to_ascii(image, new_width)
    print(image_ascii)
    return image_ascii


if __name__ == "__main__":
    import sys

    image_file_path = sys.argv[1]
    handle_image_conversion(image_file_path)
