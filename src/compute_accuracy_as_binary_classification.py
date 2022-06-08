import pandas

from convert_to_binary_classes import convert_to_binary_classes

def compute_accuracy_as_binary_classification(frame:pandas.DataFrame):
    """Converts the columns predicted_classes and actual_classes to binary data and computes the accuracy

    Args:
        frame (pandas.DataFrame): The frame to modify
    """
    frame["predicted_classes"] = frame["predicted_classes"].apply(convert_to_binary_classes)
    frame["actual_classes"] = frame["actual_classes"].apply(convert_to_binary_classes)
    frame["accuracy"] = (frame["predicted_classes"] == frame["actual_classes"]).astype(int)
