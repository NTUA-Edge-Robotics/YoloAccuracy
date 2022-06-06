import pathlib
from time import perf_counter_ns
import pydarknet

from yolo_utils import load_image

from dataset_utils import get_actual_classes
from jxl_utils import convert_image_to_jxl, convert_jxl_to_png
from image_utils import resize_image_keep_aspect_ratio

def process_image(path:pathlib.Path, height:int, quality:int, resampling:int, model:pydarknet.Detector, temp_resized:str, temp_jxl:str, temp_png:str):
    # Resize the image
    resize_image_keep_aspect_ratio(str(path), temp_resized, height)

    # Convert the image to JXL
    convert_image_to_jxl(temp_resized, temp_jxl, quality, resampling=resampling)

    # Save the image as a PNG
    convert_jxl_to_png(temp_jxl, temp_png)

    # Load the PNG as a darknet image
    darknet_image = load_image(temp_png)

    # Use YOLO to do the inference and mesure its duration (nanoseconds converted to seconds)
    start = perf_counter_ns()
    results = model.detect(darknet_image)
    end = perf_counter_ns()

    inference_time = (end - start) / 1000000000

    # Format results
    predicted_classes = [item[0] for item in results]
    confidences = [item[1] for item in results]

    # Get the actual classes in the image
    actual_classes = get_actual_classes(path.name)

    # Build the results
    results = {
        "image": path.name,
        "height": height,
        "quality": quality,
        "resampling": resampling,
        "predicted_classes": [predicted_classes],
        "confidence": [confidences],
        "actual_classes": [actual_classes],
        "inference_time": inference_time
    }

    return results
