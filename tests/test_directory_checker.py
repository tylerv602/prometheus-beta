import os
import pytest
import tempfile
import shutil

from src.directory_checker import check_directory_exists

def test_existing_directory():
    """Test that an existing directory returns True."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert check_directory_exists(temp_dir) is True

def test_non_existing_directory():
    """Test that a non-existing directory returns False."""
    # Use a path that is extremely unlikely to exist
    non_existent_path = "/tmp/this_directory_should_not_exist_12345"
    assert check_directory_exists(non_existent_path) is False

def test_file_path():
    """Test that a file path returns False."""
    with tempfile.NamedTemporaryFile() as temp_file:
        assert check_directory_exists(temp_file.name) is False

def test_none_input():
    """Test that None input raises a TypeError."""
    with pytest.raises(TypeError, match="Path cannot be None"):
        check_directory_exists(None)

def test_user_home_directory():
    """Test that user home directory resolves correctly."""
    home_path = os.path.expanduser("~")
    assert check_directory_exists(home_path) is True

def test_relative_path():
    """Test relative path resolution."""
    # Create a temporary directory and test relative path
    with tempfile.TemporaryDirectory() as temp_parent:
        # Create a subdirectory
        sub_dir = os.path.join(temp_parent, "test_subdir")
        os.makedirs(sub_dir)
        
        # Change current working directory
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_parent)
            assert check_directory_exists("test_subdir") is True
        finally:
            # Restore original working directory
            os.chdir(original_cwd)