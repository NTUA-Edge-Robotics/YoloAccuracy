import subprocess

def convert_image_to_jxl(intput:str, output:str, quality:int, resampling:int = -1):
    """Converts an image file to a JXL using cjxl.

    cjxl must be installed and be available in the path.

    Args:
        intput (str): The path to the image file to convert. The allowed images types are the one supported by cjxl (i.e. PNG, APNG, GIF, JPEG, EXR, PPM, PFM, or PGX)
        output (str): The path to the JXL file to write. Must include the .jxl extension
        quality (int): The quality factor of the JXL encoding from -inf to 100
        resampling (int, optional): Subsample all color channels by this factor. Allowed values are -1, 0, 1, 2, 4 and 8. Defaults to -1 (disabled).
    
    Raises:
        ValueError: If quality is not between 0 and 100
        ValueError: If resampling is not -1, 0, 1, 2, 4 or 8
        CalledProcessError : If the cjxl process returns a non-zero exit code (e.g. file not found, input is not a valid type, etc.)

    Examples:
        >>> convert_image_to_jxl("path/to/input.png", "path/to/output.jxl", 75)

        >>> convert_image_to_jxl("path/to/input.png", "path/to/output.jxl", 40, 8)
    
    TODO:
        Log all messages returned by cjxl
    """
    if quality > 100:
        raise ValueError("quality must be -inf to 100")
    
    if resampling not in [-1, 0, 1, 2, 4, 8]:
        raise ValueError("resampling must be between -1, 0, 1, 2, 4 or 8")

    if resampling == -1:
        process = subprocess.run(["cjxl", intput, "-q", str(quality), output], capture_output=True)
    else:
        process = subprocess.run(["cjxl", intput, "-q", str(quality), f"--resampling={resampling}", output], capture_output=True)

    process.check_returncode()

def convert_jxl_to_png(input:str, output:str):
    """Converts a JXL file to PNG using djxl.

    djxl must be installed and be available in the path.

    Args:
        input (str): The path to the JXL file to convert
        output (str): The path to the PNG file to write. Must include the .png extension
    
    Raises:
        CalledProcessError : If the djxl process returns a non-zero exit code (e.g. file not found, input is not a JXL, etc.)

    Examples:
        >>> convert_jxl_to_png("path/to/input.jxl", "path/to/output.png")

    TODO:
        Log all messages returned by djxl
    """
    process = subprocess.run(["djxl", input, output], capture_output=True)

    process.check_returncode()
