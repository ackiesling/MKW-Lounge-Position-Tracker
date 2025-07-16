#!/bin/bash

# Compile the program
g++ -I. placement_store.cpp -o mario_kart_tracker

# Check if compilation succeeded
if [ $? -eq 0 ]; then
    echo "Compiled successfully. Running the program..."
    ./mario_kart_tracker
else
    echo "Compilation failed."
fi