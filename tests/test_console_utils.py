import pytest
import sys
import io
from src.console_utils import clear_console_and_log
import os

def test_clear_console_and_log_no_message():
    """Test console clearing without a message"""
    result = clear_console_and_log()
    assert result is True

def test_clear_console_and_log_with_message():
    """Test console clearing with a message"""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    test_message = "Test logging message"
    result = clear_console_and_log(test_message)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result is True
    assert captured_output.getvalue().strip() == test_message

def test_clear_console_and_log_empty_message():
    """Test console clearing with an empty string message"""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    result = clear_console_and_log("")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result is True
    assert captured_output.getvalue().strip() == ""

def test_clear_console_and_log_none_message():
    """Test console clearing with None message"""
    result = clear_console_and_log(None)
    assert result is True