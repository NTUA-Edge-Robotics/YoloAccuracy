import os
from pathlib import Path
import pandas
import argparse

from yolo_utils import load_model
from process_image import process_image
from range_action import RangeAction

# Parse the arguments of the command line
parser = argparse.ArgumentParser(description="Benchmark YOLO with JPEG XL images")

parser.add_argument("-i", "-images", required=True, help="The directory containing the images", dest="images")
parser.add_argument("-q", "-qualities", required=True, nargs=3, type=int, action=RangeAction, help="The JPEG XL qualities to use [min] [max] [step]. max is included in the range.", dest="qualities")
parser.add_argument("-he", "-heights", required=True, nargs=3, type=int, action=RangeAction, help="The heights of the images to use [min] [max] [step]. max is included in the range.", dest="heights")
parser.add_argument("-r", "-resampling", required=True, nargs="+", type=int, help="The list of resampling values to use. Valid values are : -1, 0, 1, 2, 4, 8", dest="resampling_factors")
parser.add_argument("-t", "-temp", required=True, help="The directory to save the temporary files", dest="temp")
parser.add_argument("-j", "-json", required=True, help="Path to save the JSON results", dest="jsonPath")
parser.add_argument("-c", "-config", required=True, help="Path to the YOLO config files", dest="configPath")
parser.add_argument("-w", "-weights", required=True, help="Path to the YOLO weights", dest="weightsPath")
parser.add_argument("-m", "-meta", required=True, help="Path to the coco.data file", dest="metaPath")

args = parser.parse_args()

print(args)

# Create the temp directory
os.makedirs(args.temp, exist_ok = True)

temp_jxl = args.temp + os.sep + "temp.jxl"
temp_png = args.temp + os.sep + "temp.png"

# Load the YOLO model
model = load_model(args.configPath, args.weightsPath, args.metaPath)

# Prepare the results data frame
frame = pandas.DataFrame()

paths = Path(args.images).rglob("*")

for path in paths:
    # Skip directories
    if not path.is_file():
        continue
    
    for height in args.heights:
        for quality in args.qualities:
            for resampling in args.resampling_factors:
                temp_resized = args.temp + os.sep + "temp" + path.suffix

                results = process_image(path, height, quality, resampling, model, temp_resized, temp_jxl, temp_png)

                # Add the results to the data frame
                temp_frame = pandas.DataFrame(results)
                frame = pandas.concat([frame, temp_frame], ignore_index=True)

                # Save the results to JSON
                frame.to_json(args.jsonPath)
