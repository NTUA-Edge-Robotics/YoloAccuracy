import argparse
import pandas

from compute_accuracy_as_binary_classification import compute_accuracy_as_binary_classification

parser = argparse.ArgumentParser(description="Visualize the average accuracy of YOLO predictions according to the quality factor and the effort.")

parser.add_argument("json", help="Path to the JSON results")

args = parser.parse_args()

frame = pandas.read_json(args.json)

# Convert predicted and actual classes to a binary classification
compute_accuracy_as_binary_classification(frame)

# Group by quality and effort
frame = frame.groupby(["quality", "effort"], as_index = False)["accuracy"].mean()

frame = frame.pivot(index="quality", columns="effort", values="accuracy")

print(frame)
