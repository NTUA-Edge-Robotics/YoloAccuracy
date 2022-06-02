import os
import pathlib
from timeit import default_timer as timer
import pandas

from jxl_utils import convert_image_to_jxl, convert_jxl_to_png
from yolo_utils import load_model, load_image
from image_utils import resize_image_keep_aspect_ratio

# Parameters
configPath = "ressources" + os.sep + "yolov3.cfg"
weightsPath = "ressources" + os.sep + "yolov3.weights"
metaPath = "ressources" + os.sep + "coco.data"

images = [
    "images" + os.sep + "test.png",
    "images" + os.sep + "cat.jpg"
] # TODO Replace with a directory

quality = 30 # TODO
height = 500 # TODO
temp_jxl = "images" + os.sep + "temp.jxl"
temp_png = "images" + os.sep + "temp.png"
json_results = "ressources/results.json"

# Load the YOLO model
model = load_model(configPath, weightsPath, metaPath)

# Prepare the results data frame
frame = pandas.DataFrame()

for image in images:
    path = pathlib.Path(image)
    image_name = path.name
    extension = path.suffix
    temp_resized = "images" + os.sep + "temp" + extension

    # Resize the image
    resize_image_keep_aspect_ratio(image, temp_resized, height)

    # Convert the image to JXL
    convert_image_to_jxl(temp_resized, temp_jxl, quality)

    # Save the image as a PNG
    convert_jxl_to_png(temp_jxl, temp_png)

    # Load the PNG as a darknet image
    darknet_image = load_image(temp_png)

    # Use YOLO to do the inference and mesure its duration
    start = timer()
    results = model.detect(darknet_image)
    end = timer()

    inference_time = end - start

    # Format results
    predicted_classes = []
    confidences = []

    for predicted_class, confidence, bounds in results:
        predicted_classes.append(predicted_class)
        confidences.append(confidence)

    # TODO Get the actual classes in the image
    actual_classes = ["person", "car", "dog"]

    # Build the results
    results = {
        "image": image_name,
        "height": height,
        "quality": quality,
        "resampling": -1,
        "predicted_classes": [predicted_classes],
        "confidence": [confidences],
        "actual_classes": [actual_classes],
        "inference_time": inference_time
    }

    temp_frame = pandas.DataFrame(results)

    # Add the results to the data frame
    frame = pandas.concat([frame, temp_frame], ignore_index=True)

    # Save the results to JSON
    frame.to_json(json_results)
