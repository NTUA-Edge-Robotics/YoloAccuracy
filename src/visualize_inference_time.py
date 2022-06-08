import argparse
import pandas
from matplotlib import pyplot
from mpl_toolkits import mplot3d

parser = argparse.ArgumentParser(description="Visualize the average inference time of YOLO in GPU according to height and quality factor (all chroma subsampling modes)")

parser.add_argument("json", help="Path to the JSON results")

args = parser.parse_args()

frame = pandas.read_json(args.json)

f = frame.groupby(["quality", "height"], as_index = False)["inference_time"].mean()

# Prepare graph
pyplot.figure()
axes = pyplot.axes(projection="3d")

q = f["quality"]
it = f["inference_time"]
h = f["height"]

axes.bar(q, it, zs=h, zdir="y", width = 5)

# Labelling
axes.set_xlabel("Quality")
pyplot.xticks(f["quality"].unique())

axes.set_ylabel("Height (pixels)")
pyplot.yticks(f["height"].unique())

axes.set_zlabel("Average Inference Time (s)")

pyplot.title(f"The average inference time of YOLO in GPU according to height and quality factor (all chroma subsampling modes)", wrap = True)

axes.view_init(23, -139)

pyplot.show()
