import os
from pathlib import Path
import pandas
import argparse
import torch

from process_image import process_image
from range_action import RangeAction

# Parse the arguments of the command line
parser = argparse.ArgumentParser(description="Benchmark YOLO with JPEG XL images")

parser.add_argument("-i", "-images", required=True, help="The directory containing the images", dest="images")
parser.add_argument("-q", "-qualities", required=True, nargs=3, type=int, action=RangeAction, help="The JPEG XL qualities to use [min] [max] [step]. max is included in the range.", dest="qualities")
parser.add_argument("-he", "-heights", required=True, nargs=3, type=int, action=RangeAction, help="The heights of the images to use [min] [max] [step]. max is included in the range.", dest="heights")
parser.add_argument("-t", "-temp", required=True, help="The directory to save the temporary files", dest="temp")
parser.add_argument("-j", "-json", required=True, help="Path to save the JSON results", dest="jsonPath")
parser.add_argument("-m", "-model", required=True, help="The YOLOv5 model to use", dest="model")

args = parser.parse_args()

# Create the temp directory
os.makedirs(args.temp, exist_ok = True)

temp_jxl = args.temp + os.sep + "temp.jxl"
temp_png = args.temp + os.sep + "temp.png"

# Load the YOLO model
model = torch.hub.load("ultralytics/yolov5", args.model)

# Prepare the results data frame
frame = pandas.DataFrame()

paths = Path(args.images).rglob("*")

for path in paths:
    # Skip directories
    if not path.is_file():
        continue
    
    for height in args.heights:
        for quality in args.qualities:
            temp_resized = args.temp + os.sep + "temp" + path.suffix

            results = process_image(path, height, quality, model, temp_resized, temp_jxl, temp_png)

            # Add the results to the data frame
            temp_frame = pandas.DataFrame(results)
            frame = pandas.concat([frame, temp_frame], ignore_index=True)

            # Save the results to JSON
            frame.to_json(args.jsonPath)
