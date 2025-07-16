# Mario Kart Tracker

A linux terminal-based tool to record and track Mario Kart race placements.

##  Features

- Stores track names and race placements (enter tracks as lowercase eg rpb, bc, bci)
- Saves data across runs
- Undo with `back`


##  Usage
Do 'chmod +x run.sh' to ensure the shell script is executable. To use the code,
enter './run.sh' in the terminal inside of the directory containing all of the other files.
A .txt file will be created to permanently store your race data (track name and placement).
To end data collection, just do CTRL+C in your terminal line.

## Project Structure

```bash
├── placement_store.cpp
├── tracks.h
├── run.sh
└── position_data.txt   # (ignored in git)

