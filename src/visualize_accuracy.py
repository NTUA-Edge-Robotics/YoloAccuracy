import argparse
import pandas
from matplotlib import pyplot
from mpl_toolkits import mplot3d

from compute_accuracy_as_binary_classification import compute_accuracy_as_binary_classification

parser = argparse.ArgumentParser(description="Visualize the average accuracy of YOLO predictions according to height and quality factor.")

parser.add_argument("json", help="Path to the JSON results")
parser.add_argument("figure", help="Path and filename of the resulting figure")

args = parser.parse_args()

frame = pandas.read_json(args.json)

# Convert predicted and actual classes to a binary classification
compute_accuracy_as_binary_classification(frame)

frame = frame.groupby(["quality", "height"], as_index = False)["accuracy"].mean()

# Prepare graph
pyplot.figure(figsize=(3.4, 4))
axes = pyplot.axes(projection="3d")

axes.bar(frame["quality"], frame["accuracy"], zs=frame["height"], zdir="y", width = 5)

# Labelling
axes.set_xlabel("Quality")
pyplot.xticks(frame["quality"].unique(), rotation=-40)

axes.set_ylabel("Height (pixels)")
pyplot.yticks(frame["height"].unique(), rotation=50)

axes.set_zlabel("Average Accuracy")

axes.view_init(23, -139)

pyplot.tick_params(axis="both", which="both", labelsize=6)
pyplot.savefig(args.figure, bbox_inches="tight")
