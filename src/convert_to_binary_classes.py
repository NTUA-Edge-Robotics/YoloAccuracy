def convert_to_binary_classes(value:list) -> int:
    """Converts a list of classes to a binary result.

    Args:
        value (list): The list that should be converted to a binary result

    Returns:
        int: 1 if value contains person, 0 if not

    Examples:
        >>> convert_to_binary_classes(["person", "bird"])
        1

        >>> convert_to_binary_classes(["dog"])
        0

        >>> convert_to_binary_classes([])
        0
    """
    if "person" in value:
        return 1
    
    return 0
