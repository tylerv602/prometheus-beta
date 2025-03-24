import os
import json
from typing import List, Optional

class KeystrokeLogger:
    """
    A class to log keystrokes entered by the user.
    
    The logger stores keystrokes in a JSON file, allowing for persistent logging
    and easy retrieval of logged keystrokes.
    """
    
    def __init__(self, log_file: str = 'keystrokes.json'):
        """
        Initialize the KeystrokeLogger.
        
        Args:
            log_file (str, optional): Path to the log file. Defaults to 'keystrokes.json'.
        """
        self.log_file = log_file
        self._ensure_log_file()
    
    def _ensure_log_file(self):
        """
        Ensure the log file exists and is a valid JSON file.
        Creates the file if it doesn't exist.
        """
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump([], f)
    
    def log_keystroke(self, keystroke: str):
        """
        Log a single keystroke to the log file.
        
        Args:
            keystroke (str): The keystroke to log.
        
        Raises:
            ValueError: If the keystroke is empty or not a single character.
        """
        if not keystroke or len(keystroke) != 1:
            raise ValueError("Keystroke must be a single, non-empty character")
        
        # Read existing log
        with open(self.log_file, 'r') as f:
            log_entries = json.load(f)
        
        # Append new keystroke
        log_entries.append(keystroke)
        
        # Write updated log
        with open(self.log_file, 'w') as f:
            json.dump(log_entries, f)
    
    def get_keystrokes(self) -> List[str]:
        """
        Retrieve all logged keystrokes.
        
        Returns:
            List[str]: A list of logged keystrokes.
        """
        with open(self.log_file, 'r') as f:
            return json.load(f)
    
    def clear_log(self):
        """
        Clear all logged keystrokes.
        """
        with open(self.log_file, 'w') as f:
            json.dump([], f)