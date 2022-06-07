# YoloBenchmarker

The project aims to benchmark the performance of [YOLO](https://pjreddie.com/darknet/yolo/) using [JPEG XL](https://jpeg.org/jpegxl/).

## Installation

1. Install [libjxl](https://github.com/libjxl/libjxl/releases) on your computer. `cjxl` and `djxl` needs to be available on your path.
1. Install the dependencies with `pip install -r requirements.txt`

## Primary Data Generation

The API of the script can be found using `generate_primary_data.py -h`. The script follows these steps :

1. Load a raw or lossless image (e.g. PNG)
1. Resize the image (if necessary) and keep the aspect ratio
1. Save the image as JPEG XL (JXL) according to the quality factor and the chroma subsampling
1. Convert the JXL to a lossless format (PNG)
1. Detect the objects in the saved JXL with YOLO
1. Mesure the speed of the inference in seconds
1. Get the predicted classes, the confidence (%) and the actual classes
1. Save the results in a JSON file

### Notes

The script is meant to work with the [People Overhead dataset](https://www.kaggle.com/datasets/hifrom/people-overhead). To use another dataset, `dataset_utils.py` should be updated to retrieve the proper actual classes.

## Data Visualization

Wanted graphics :

- Accuracy according to quality, height and color subsampling (4 graphs)
- Confidence according to quality, height and color subsampling (?)
- Inference time according to quality, height and color subsampling

## What needs to be done

- Generate the secondary data
- Visualize the data

## What could be improved

- Log and handle errors
- Automated tests
