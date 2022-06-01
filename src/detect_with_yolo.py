from timeit import default_timer as timer
from datetime import timedelta

from pydarknet import Detector, Image
import cv2

config = bytes("ressources/yolov3.cfg", encoding="utf-8")
weights = bytes("ressources/yolov3.weights", encoding="utf-8")
labels = bytes("ressources/coco.data", encoding="utf-8")
image = "images/test.png"

net = Detector(config, weights, 0, labels)

img = cv2.imread(image)
img_darknet = Image(img)

start = timer()

results = net.detect(img_darknet)

end = timer()
    
for category, score, bounds in results:
    print(category, score, "confidence")

print("Elapsed Time", timedelta(seconds=end-start))