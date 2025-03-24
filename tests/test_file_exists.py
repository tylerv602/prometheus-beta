import os
import pytest
import tempfile

from src.file_exists import file_exists

def test_file_exists_with_existing_file():
    """Test that file_exists returns True for an existing file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert file_exists(temp_file_path) is True
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_file_exists_with_non_existing_file():
    """Test that file_exists returns False for a non-existing file."""
    # Use a path that almost certainly doesn't exist
    non_existent_path = "/path/to/definitely/non/existing/file.txt"
    assert file_exists(non_existent_path) is False

def test_file_exists_with_directory():
    """Test that file_exists returns False for a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert file_exists(temp_dir) is False

def test_file_exists_with_invalid_input():
    """Test that file_exists raises TypeError for non-string inputs."""
    with pytest.raises(TypeError, match="File path must be a string"):
        file_exists(123)
    
    with pytest.raises(TypeError, match="File path must be a string"):
        file_exists(None)

def test_file_exists_with_empty_string():
    """Test that file_exists handles empty string input."""
    assert file_exists("") is False