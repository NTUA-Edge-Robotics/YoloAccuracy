import re

def get_actual_classes(image_name:str) -> list:
    """Gets the actual classes of an image using the image name.

    This function is intented to work with the "People Overhead" dataset

    Args:
        input (str): The name of the image file. The name should start with the number of persons in the image

    Returns:
        list: A list containing the string "person" n times. n is the number of persons in the image.

        If the image name is not properly formatted, an empty list is returned.

    Examples:
        >>> get_actual_classes("5 (138)")
        ["person", "person", "person", "person", "person"]
    """
    groups = re.compile("^(\d+)").match(image_name)

    if (groups is None):
        return []
    
    num_persons = int(groups.group(1))

    return ["person"] * num_persons
