import os
import gzip
import pytest
from src.gzip_decompress import decompress_gzip_file

@pytest.fixture
def sample_gzip_file(tmp_path):
    """Create a sample gzip file for testing."""
    input_file = tmp_path / "sample.txt.gz"
    with gzip.open(input_file, 'wb') as f:
        f.write(b"Hello, this is a test file for gzip decompression!")
    return input_file

def test_successful_decompression(sample_gzip_file, tmp_path):
    """Test successful gzip file decompression."""
    output_file = tmp_path / "sample.txt"
    
    # Decompress the file
    result = decompress_gzip_file(str(sample_gzip_file), str(output_file))
    
    # Verify the output file exists and has correct content
    assert os.path.exists(output_file)
    with open(output_file, 'rb') as f:
        content = f.read()
        assert content == b"Hello, this is a test file for gzip decompression!"
    assert result == str(output_file)

def test_default_output_filename(sample_gzip_file, tmp_path):
    """Test decompression with default output filename."""
    # Decompress without specifying output file
    result = decompress_gzip_file(str(sample_gzip_file))
    
    # Verify the output file exists and has correct name
    expected_output = str(sample_gzip_file).removesuffix('.gz')
    assert os.path.exists(expected_output)
    assert result == expected_output

def test_nonexistent_input_file():
    """Test handling of non-existent input file."""
    with pytest.raises(FileNotFoundError):
        decompress_gzip_file("nonexistent_file.gz")

def test_invalid_gzip_file(tmp_path):
    """Test handling of invalid gzip file."""
    invalid_gzip = tmp_path / "invalid.gz"
    with open(invalid_gzip, 'wb') as f:
        f.write(b"This is not a valid gzip file")
    
    with pytest.raises(ValueError, match="Invalid gzip file"):
        decompress_gzip_file(str(invalid_gzip))