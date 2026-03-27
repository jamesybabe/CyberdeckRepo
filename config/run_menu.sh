#!/bin/bash

echo "Select a file:"
files=(*.py *.sh *.txt)

# Show numbered list
for i in "${!files[@]}"; do
    echo "$((i+1))) ${files[$i]}"
done

# Get user input
read -p "Enter number: " choice

# Convert to array index
index=$((choice-1))
selected="${files[$index]}"

# Check if selection exists
if [ -z "$selected" ]; then
    echo "Invalid selection"
    exit 1
fi

echo "Selected: $selected"

# Ask mode
read -p "Run or view? (r/v): " mode

if [[ $mode == "v" ]]; then
    less "$selected"
    exit
fi

echo "Running: $selected"

# Decide how to run based on file type
if [[ $selected == *.py ]]; then
    python "$selected"
elif [[ $selected == *.sh ]]; then
    bash "$selected"
elif [[ $selected == *.txt ]]; then
    bash "$selected"
else
    echo "Don't know how to run this file"
fi