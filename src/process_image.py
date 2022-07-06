import pathlib

from dataset_utils import get_actual_classes
from jxl_utils import convert_image_to_jxl, convert_jxl_to_png
from image_utils import resize_image_keep_aspect_ratio

def process_image(path:pathlib.Path, height:int, quality:int, model, temp_resized:str, temp_jxl:str, temp_png:str):
    # Resize the image
    resize_image_keep_aspect_ratio(str(path), temp_resized, height)

    # Convert the image to JXL
    convert_image_to_jxl(temp_resized, temp_jxl, quality)

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
        "predicted_classes": [predicted_classes],
        "confidence": [confidences],
        "actual_classes": [actual_classes],
        "inference_time": [results.t]
    }

    return results
