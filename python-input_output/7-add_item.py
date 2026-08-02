#!/usr/bin/python3
"""
This module provides a script that adds all command-line arguments
to a Python list and saves them to a JSON file.
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"

    # Check if file exists and is not empty to safely load existing items
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        try:
            my_list = load_from_json_file(filename)
        except (FileNotFoundError, ValueError):
            my_list = []
    else:
        my_list = []

    # Append all arguments passed to the script (skipping the script name)
    my_list.extend(sys.argv[1:])

    # Save the updated list back to the JSON file
    save_to_json_file(my_list, filename)

