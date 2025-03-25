import os

def are_files_identical(file1_path, file2_path):
    """
    Compare two files and check if they are identical.

    Args:
        file1_path (str): Path to the first file
        file2_path (str): Path to the second file

    Returns:
        bool: True if files are identical, False otherwise

    Raises:
        FileNotFoundError: If either file does not exist
        PermissionError: If there are permission issues reading the files
        IsADirectoryError: If either path is a directory
    """
    # Check if paths are files (not directories)
    if os.path.isdir(file1_path):
        raise IsADirectoryError(f"First path is a directory: {file1_path}")
    if os.path.isdir(file2_path):
        raise IsADirectoryError(f"Second path is a directory: {file2_path}")

    # Check if files exist
    if not os.path.exists(file1_path):
        raise FileNotFoundError(f"First file not found: {file1_path}")
    if not os.path.exists(file2_path):
        raise FileNotFoundError(f"Second file not found: {file2_path}")

    # Check file sizes first (quick initial comparison)
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False

    # Compare file contents
    with open(file1_path, 'rb') as f1, open(file2_path, 'rb') as f2:
        # Read and compare files in chunks to handle large files
        while True:
            chunk1 = f1.read(4096)
            chunk2 = f2.read(4096)

            # If both chunks are empty, files are identical
            if not chunk1 and not chunk2:
                return True

            # If chunks differ, files are not identical
            if chunk1 != chunk2:
                return False