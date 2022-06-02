import cv2

def resize_image_keep_aspect_ratio(input:str, output:str, height:int):
    """Resizes an image with OpenCV and keep the original aspect ratio.

    Args:
        input (str): The path to the image file to resize. The allowed images types are the one supported by OpenCV
        output (str): The path to the image file to write. Must include the extension
        height (int): The new height of the image in pixels.

    Raises:
        ValueError: If height is smaller than 1 or bigger than the input height

    Examples:
        >>> resize_image_keep_aspect_ratio("path/to/input.jpg", "path/to/output.png", 500)
    """
    image = cv2.imread(input)
    ratio = height / image.shape[0]

    if height < 1 or image > image.shape[0]:
        raise ValueError("height must be bigger than 0 and smaller than the input height")

    image = cv2.resize(image, (0, 0), fx = ratio, fy = ratio)

    cv2.imwrite(output, image)
