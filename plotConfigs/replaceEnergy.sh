#!/bin/bash

# Directory containing the Python files
directory_path="./"

# Search and replace strings
search_string="3 TeV"
replace_string="2.8 TeV"

# Find all Python files in the directory and apply the replacement
find "$directory_path" -type f -name '*.py' | while read -r file; do
    # Use sed to replace the string in the file
    sed -i "s|$search_string|$replace_string|g" "$file"
done
