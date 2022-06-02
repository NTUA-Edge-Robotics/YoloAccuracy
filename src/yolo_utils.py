import pydarknet
import cv2

def load_model(config_path:str, weights_path:str, meta_path:str) -> pydarknet.Detector:
    """Loads and initialize a darknet model

    Args:
        config_path (str): The path to the model configuration file
        weights_path (str): The path to the models weights
        meta_path (str): The path to the coco.data file

    Returns:
        pydarknet.Detector: The darknet model

    Examples:
        >>> load_model("path/to/yolov3.cfg", "path/to/yolov3.weights", "path/to/coco.data")
    """
    config = bytes(config_path, encoding="utf-8")
    weights = bytes(weights_path, encoding="utf-8")
    meta = bytes(meta_path, encoding="utf-8")

    return pydarknet.Detector(config, weights, 0, meta)

def load_image(input:str) -> pydarknet.Image:
    """Loads an image using OpenCV and convert it to a darknet image

    Args:
        input (str): The path to the image to load

    Returns:
        pydarknet.Image: The darknet image

    Examples:
        >>> load_image("path/to/input.png")
    """
    image = cv2.imread(input)
    
    return pydarknet.Image(image)
