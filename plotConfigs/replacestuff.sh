#!/bin/bash

# Directory containing the Python files
directory_path="$PWD"

# Array of search and replace strings
declare -a replacements=(
    "run_0p5/run_100001"
    "run_1p0/run_100002"
    "run_1p4/run_100003"
    "run_2p0/run_100004"
    "run_2p5/run_100005"
    "run_3p0/run_100006"
)

# Find all Python files in the directory and apply the replacements
find "$directory_path" -type f -name '*.py' | while read -r file; do
    for pair in "${replacements[@]}"; do
        # Split the pair into original and replacement
        IFS="/" read -r original replacement <<< "$pair"
        # Use sed to replace the line in the file
        sed -i "s|\"filePath\"    :   \"/afs/cern.ch/work/s/sgoswami/public/taunvnvlq/${original}/out.root\"|\"filePath\"    :   \"/afs/cern.ch/work/s/sgoswami/public/taunvnvlq/${replacement}/out.root\"|g" "$file"
    done
done
