import gzip
import os

def decompress_gzip_file(input_filepath, output_filepath=None):
    """
    Decompress a gzip file to a specified output path.

    Args:
        input_filepath (str): Path to the input gzip file.
        output_filepath (str, optional): Path to save the decompressed file. 
                                         If not provided, uses input filepath without .gz extension.

    Returns:
        str: Path to the decompressed file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        IOError: If there are issues reading or writing files.
        ValueError: If the input file is not a valid gzip file.
    """
    # Validate input file exists
    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"Input file not found: {input_filepath}")

    # Determine output filepath if not provided
    if output_filepath is None:
        # Remove .gz extension if present
        output_filepath = input_filepath.removesuffix('.gz')
        if output_filepath == input_filepath:
            output_filepath += '.decompressed'

    try:
        # Open and read the gzip file
        with gzip.open(input_filepath, 'rb') as f_in:
            # Write the decompressed content to output file
            with open(output_filepath, 'wb') as f_out:
                f_out.write(f_in.read())
        
        return output_filepath

    except gzip.BadGzipFile:
        raise ValueError(f"Invalid gzip file: {input_filepath}")
    except IOError as e:
        raise IOError(f"Error processing gzip file: {str(e)}")