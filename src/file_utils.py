import os


def file_exists(file_path: str) -> bool:
    """
    Check if a file exists at the specified path.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file exists and is a file, False otherwise.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input type
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Normalize the path and check if it exists and is a file
    try:
        return os.path.isfile(os.path.expanduser(file_path))
    except TypeError:
        # Handle cases with invalid path types
        return False