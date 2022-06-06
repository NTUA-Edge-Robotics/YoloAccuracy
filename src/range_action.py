import argparse

class RangeAction(argparse.Action):
    """Transforms an argument to a range.

    The argument must be a list of 3 integers : [min] [max] [step].

    max is included in the range.
    """
    def __call__(self, parser:argparse.ArgumentParser, namespace:argparse.Namespace, values, option_string=None):
        """
        Raises:
            ArgumentTypeError: When values does not contain 3 elements
        """
        if (len(values) != 3):
            raise argparse.ArgumentTypeError("A value is missing. Should be [min] [max] [step]")
        
        min = values[0]
        max = values[1] + 1 # +1 to include max in the range
        step = values[2]

        my_range = range(min, max, step)

        setattr(namespace, self.dest, my_range)
