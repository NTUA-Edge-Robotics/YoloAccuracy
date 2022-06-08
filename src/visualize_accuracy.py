import argparse
import pandas
from matplotlib import pyplot
from mpl_toolkits import mplot3d

from compute_accuracy_as_binary_classification import compute_accuracy_as_binary_classification

parser = argparse.ArgumentParser(description="Visualize the average accuracy of YOLO predictions according to height and quality factor with a specific chroma subsampling factor")

parser.add_argument("json", help="Path to the JSON results")
parser.add_argument("resampling", type=int, help="The chroma subsampling factor to isolate")

args = parser.parse_args()

frame = pandas.read_json(args.json)

# Convert predicted and actual classes to a binary classification
compute_accuracy_as_binary_classification(frame)

# Keep only pictures where there are people
persons = frame.query("actual_classes == 1")

# Separate results by chroma subsampling mode
chroma = persons.query(f"resampling == {args.resampling}")
f = chroma.groupby(["quality", "height"], as_index = False)["accuracy"].mean()

# Prepare graph
pyplot.figure()
axes = pyplot.axes(projection="3d")

q = f["quality"]
a = f["accuracy"]
h = f["height"]

axes.bar(q, a, zs=h, zdir="y", width = 5)

# Labelling
axes.set_xlabel("Quality")
pyplot.xticks(f["quality"].unique())

axes.set_ylabel("Height (pixels)")
pyplot.yticks(f["height"].unique())

axes.set_zlabel("Average Accuracy")

pyplot.title(f"The average accuracy of YOLO predictions according to height and quality factor with chroma subsampling factor of {args.resampling}", wrap = True)

axes.view_init(23, -139)

pyplot.show()
