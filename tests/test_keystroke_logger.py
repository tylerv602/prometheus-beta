import os
import pytest
import json
from src.keystroke_logger import KeystrokeLogger

def test_keystroke_logger_initialization():
    """Test that the logger creates a log file if it doesn't exist."""
    log_file = 'test_keystrokes.json'
    
    # Ensure file doesn't exist before initialization
    if os.path.exists(log_file):
        os.remove(log_file)
    
    logger = KeystrokeLogger(log_file)
    
    # Check that file was created
    assert os.path.exists(log_file)
    
    # Check that file contains an empty list
    with open(log_file, 'r') as f:
        content = json.load(f)
        assert content == []

def test_log_single_keystroke():
    """Test logging a single valid keystroke."""
    log_file = 'test_keystrokes.json'
    logger = KeystrokeLogger(log_file)
    
    # Clear any existing log
    logger.clear_log()
    
    # Log a keystroke
    logger.log_keystroke('a')
    
    # Verify keystroke was logged
    keystrokes = logger.get_keystrokes()
    assert len(keystrokes) == 1
    assert keystrokes[0] == 'a'

def test_log_multiple_keystrokes():
    """Test logging multiple keystrokes."""
    log_file = 'test_keystrokes.json'
    logger = KeystrokeLogger(log_file)
    
    # Clear any existing log
    logger.clear_log()
    
    # Log multiple keystrokes
    test_keys = ['h', 'e', 'l', 'l', 'o']
    for key in test_keys:
        logger.log_keystroke(key)
    
    # Verify keystrokes were logged
    keystrokes = logger.get_keystrokes()
    assert keystrokes == test_keys

def test_invalid_keystroke_logging():
    """Test that logging invalid keystrokes raises an error."""
    logger = KeystrokeLogger('test_keystrokes.json')
    
    # Try logging empty string
    with pytest.raises(ValueError, match="Keystroke must be a single, non-empty character"):
        logger.log_keystroke('')
    
    # Try logging multiple characters
    with pytest.raises(ValueError, match="Keystroke must be a single, non-empty character"):
        logger.log_keystroke('ab')

def test_clear_log():
    """Test clearing the log."""
    log_file = 'test_keystrokes.json'
    logger = KeystrokeLogger(log_file)
    
    # Log some keystrokes
    logger.log_keystroke('a')
    logger.log_keystroke('b')
    
    # Clear the log
    logger.clear_log()
    
    # Verify log is empty
    keystrokes = logger.get_keystrokes()
    assert len(keystrokes) == 0