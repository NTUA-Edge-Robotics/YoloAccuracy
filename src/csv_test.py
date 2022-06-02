import csv

file = open("ressources/results.csv", "a")
csv_results = csv.DictWriter(file, ["image", "height", "quality", "resampling", "predicted_classes", "confidence", "actual_classes", "inference_time"])
csv_results.writeheader()