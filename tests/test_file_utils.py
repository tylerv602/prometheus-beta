import os
import pytest
import tempfile

from src.file_utils import file_exists


def test_file_exists_with_existing_file():
    """Test that file_exists returns True for an existing file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        try:
            assert file_exists(temp_file.name) is True
        finally:
            os.unlink(temp_file.name)


def test_file_exists_with_nonexistent_file():
    """Test that file_exists returns False for a nonexistent file."""
    assert file_exists("/path/to/nonexistent/file.txt") is False


def test_file_exists_with_directory():
    """Test that file_exists returns False for a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert file_exists(temp_dir) is False


def test_file_exists_with_invalid_input_types():
    """Test that file_exists raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        file_exists(None)
    
    with pytest.raises(TypeError):
        file_exists(123)
    
    with pytest.raises(TypeError):
        file_exists(["file.txt"])


def test_file_exists_with_expanded_path():
    """Test that file_exists works with expanded user paths."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        try:
            home_path = os.path.join("~", os.path.basename(temp_file.name))
            assert file_exists(home_path) is False
        finally:
            os.unlink(temp_file.name)