import os
import pytest
import tempfile
import shutil

from src.file_comparison import are_files_identical

def test_identical_files():
    """Test that identical files return True"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create two identical files
        file1 = os.path.join(tmpdir, 'file1.txt')
        file2 = os.path.join(tmpdir, 'file2.txt')
        
        with open(file1, 'w') as f1, open(file2, 'w') as f2:
            f1.write("Hello, world!")
            f2.write("Hello, world!")
        
        assert are_files_identical(file1, file2) == True

def test_different_files():
    """Test that different files return False"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create two different files
        file1 = os.path.join(tmpdir, 'file1.txt')
        file2 = os.path.join(tmpdir, 'file2.txt')
        
        with open(file1, 'w') as f1, open(file2, 'w') as f2:
            f1.write("Hello, world!")
            f2.write("Hello, world!")
        
        with open(file1, 'a') as f1:
            f1.write(" Extra content")
        
        assert are_files_identical(file1, file2) == False

def test_empty_files():
    """Test that two empty files are identical"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create two empty files
        file1 = os.path.join(tmpdir, 'file1.txt')
        file2 = os.path.join(tmpdir, 'file2.txt')
        
        open(file1, 'w').close()
        open(file2, 'w').close()
        
        assert are_files_identical(file1, file2) == True

def test_file_not_found():
    """Test that FileNotFoundError is raised for non-existent files"""
    with tempfile.TemporaryDirectory() as tmpdir:
        non_existent_file = os.path.join(tmpdir, 'non_existent.txt')
        existing_file = os.path.join(tmpdir, 'existing.txt')
        
        with open(existing_file, 'w') as f:
            f.write("Some content")
        
        # Test non-existent first file
        with pytest.raises(FileNotFoundError):
            are_files_identical(non_existent_file, existing_file)
        
        # Test non-existent second file
        with pytest.raises(FileNotFoundError):
            are_files_identical(existing_file, non_existent_file)

def test_directory_input():
    """Test that IsADirectoryError is raised when directory is passed"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Test with first argument as directory
        with pytest.raises(IsADirectoryError):
            are_files_identical(tmpdir, os.path.join(tmpdir, 'file.txt'))
        
        # Test with second argument as directory
        test_file = os.path.join(tmpdir, 'file.txt')
        with open(test_file, 'w') as f:
            f.write("Some content")
        
        with pytest.raises(IsADirectoryError):
            are_files_identical(test_file, tmpdir)

def test_large_files():
    """Test comparison of large files"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create two large files with same content
        file1 = os.path.join(tmpdir, 'large1.txt')
        file2 = os.path.join(tmpdir, 'large2.txt')
        
        # Create a 1MB file
        with open(file1, 'wb') as f1, open(file2, 'wb') as f2:
            content = b'A' * (1024 * 1024)
            f1.write(content)
            f2.write(content)
        
        assert are_files_identical(file1, file2) == True

        # Modify one file slightly
        with open(file1, 'ab') as f1:
            f1.write(b'Extra')
        
        assert are_files_identical(file1, file2) == False