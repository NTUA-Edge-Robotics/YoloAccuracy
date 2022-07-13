import pathlib

from dataset_utils import get_actual_classes
from jxl_utils import convert_image_to_jxl, convert_jxl_to_png
from image_utils import resize_image_keep_aspect_ratio

def process_image(path:pathlib.Path, height:int, quality:int, effort:str, model:str, temp_resized:str, temp_jxl:str, temp_png:str):
    """Converts one image to JPEG XL, runs the inference with YOLOv5 and returns the results.

    Args:
        path (pathlib.Path): The path to the image to run the inference
        height (int): The height of the image in pixels. Aspect ratio is kept
        quality (int): The quality factor of the image between -Inf to 100
        effort (str): The name of the effort (e.g. lightning, thunder, etc.) for the JXL encoding
        model (str): The name of the YOLOv5 model to use
        temp_resized (str): The name of the temporary image that will be resized
        temp_jxl (str): The name of the temporary image that will be converted to JXL
        temp_png (str): The name of the temporary JXL image that will be converted to PNG and used to run the inference

    Returns:
        dict[str, any]: The name of the image, its height, its quality factor, the predicted classes, the confidence of the predictions, the actual classes and the inference time
    """
    # Resize the image
    resize_image_keep_aspect_ratio(str(path), temp_resized, height)

    # Convert the image to JXL
    convert_image_to_jxl(temp_resized, temp_jxl, quality, effort)

    # Save the image as a PNG
    convert_jxl_to_png(temp_jxl, temp_png)

    # Use YOLO to do the inference
    results = model(temp_png)

    # Get results
    predicted_classes = [results.names[int(item[5].item())] for item in results.pred[0]]
    confidences = [item[4].item() for item in results.pred[0]]

    # Get the actual classes in the image
    actual_classes = get_actual_classes(path.name)

    # Build the results
    results = {
        "image": path.name,
        "height": height,
        "quality": quality,
        "effort": effort,
        "predicted_classes": [predicted_classes],
        "confidence": [confidences],
        "actual_classes": [actual_classes],
        "inference_time": [results.t]
    }

    return results
