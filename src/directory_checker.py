import os
from typing import Union, Optional, AnyStr

def check_directory_exists(path: Union[str, bytes, os.PathLike]) -> bool:
    """
    Check if a directory exists at the specified path.

    Args:
        path (Union[str, bytes, os.PathLike]): The path to the directory to check.

    Returns:
        bool: True if the path exists and is a directory, False otherwise.

    Raises:
        TypeError: If the input path is None.
    """
    # Check for None input
    if path is None:
        raise TypeError("Path cannot be None")

    # Expand user and normalize path
    expanded_path = os.path.expanduser(path)
    
    # Check if path exists and is a directory
    return os.path.isdir(expanded_path)