# file_manager.py

import os
import logging

def list_files(directory):
    """List all files in a directory."""
    try:
        files = os.listdir(directory)
        return f"Files in '{directory}':\n" + "\n".join(files)
    except Exception as e:
        return f"Error listing files: {e}"

def read_file(filepath):
    """Read the contents of a file."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        return f"Contents of '{filepath}':\n{content}"
    except Exception as e:
        return f"Error reading file: {e}"

def write_file(filepath, content):
    """Write content to a file."""
    try:
        with open(filepath, 'w') as file:
            file.write(content)
        return f"File '{filepath}' written successfully."
    except Exception as e:
        return f"Error writing file: {e}"

def delete_file(filepath):
    """Delete a file."""
    try:
        os.remove(filepath)
        return f"File '{filepath}' deleted successfully."
    except Exception as e:
        return f"Error deleting file: {e}"