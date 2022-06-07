import os
import pandas
from matplotlib import pyplot
from mpl_toolkits import mplot3d

from convert_to_binary_classes import convert_to_binary_classes

json_path = "ressources" + os.sep + "results.json"
frame = pandas.read_json(json_path)

# Convert predicted and actual classes to a binary classification
frame["predicted_classes"] = frame["predicted_classes"].apply(convert_to_binary_classes)
frame["actual_classes"] = frame["actual_classes"].apply(convert_to_binary_classes)
frame["accuracy"] = (frame["predicted_classes"] == frame["actual_classes"]).astype(int)

#
chroma_minus_1 = frame.query("resampling == 8")
f = frame.groupby(["quality", "height"], as_index = False)["accuracy"].mean()

#print(accuracy_minus_1)

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

axes.set_zlabel("Average Accuracy (%)")

pyplot.title("The average accuracy of YOLO predictions according to height and quality factor with chroma subsampling disabled", wrap = True)

# pyplot.savefig(filename, format="svg")
pyplot.show()
