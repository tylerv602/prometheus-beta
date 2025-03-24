import os
import platform

def clear_console_and_log(message=None):
    """
    Clear the console screen and optionally log a message.
    
    Supports Windows, macOS, and Linux/Unix-like systems.
    
    Args:
        message (str, optional): Message to log after clearing the console. 
                                 Defaults to None.
    
    Returns:
        bool: True if console was successfully cleared, False otherwise
    """
    try:
        # Determine the operating system and use appropriate clear command
        os_name = platform.system().lower()
        
        if os_name == 'windows':
            # For Windows
            os.system('cls')
        else:
            # For Unix-like systems (macOS, Linux)
            os.system('clear')
        
        # Log message if provided
        if message is not None:
            print(message)
        
        return True
    except Exception:
        # Fallback if clearing console fails
        return False