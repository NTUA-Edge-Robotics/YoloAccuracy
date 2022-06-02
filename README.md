# YoloBenchmarker

## Primary data

The `generate_primary_data.py` script follows these steps :

1. Load a raw or lossless image (e.g. TIFF or PNG)
1. Resize the image (if necessary) and keep the aspect ratio
1. Save the image as JPEG XL (JXL) according to the quality factor and the chroma subsampling
1. Convert the JXL to a lossless format (PNG)
1. Detect the objects in the saved JXL with YOLO
1. Mesure the speed of the detection in seconds
1. Get the predicted classes, the confidence (%) and the actual classes
1. Save the results in a JSON file

## Things that needs to be defined

- The images we want to use
- The weights and the config files to use with YOLO (e.g. yolo and yolo-tiny)

## What needs to be done

- Get the actual classes in an image
- Log and handle errors
- Generate the secondary data
