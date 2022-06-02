import os
import pathlib
from timeit import default_timer as timer
from datetime import timedelta

from jxl_utils import convert_image_to_jxl, convert_jxl_to_png
from yolo_utils import load_model, load_image
from image_utils import resize_image_keep_aspect_ratio

# Load the YOLO model
configPath = "ressources" + os.sep + "yolov3.cfg"
weightsPath = "ressources" + os.sep + "yolov3.weights"
metaPath = "ressources" + os.sep + "coco.data"
images = [] # TODO
quality = 30 # TODO
temp_jxl = "images" + os.sep + "temp.jxl"
temp_png = "images" + os.sep + "temp.png"

model = load_model(configPath, weightsPath, metaPath)

for image in images:
    extension = pathlib.Path(image).suffix
    temp_resized = "images" + os.sep + "temp" + extension

    # Resize the image
    resize_image_keep_aspect_ratio(image, temp_resized, 500) # TODO Dont hardcode the height

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

    duration = timedelta(seconds=end-start)

    # Get the actual classes in the image
    # TODO

    # Save the results to CSV
    # TODO