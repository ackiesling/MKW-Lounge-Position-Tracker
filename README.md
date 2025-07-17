# Mario Kart Tracker

A linux terminal-based tool to record and track Mario Kart race placements. (I recommend using VSCode WSL for easy png viewing)

##  Features

- Store position data for every track in MKW (12 player races only)
- Multiple data visualization tools
  - Cumulative average plots for every track
  - Rankings of tracks by point averages
  - Histograms of track averages


##  Usage
- enter_tracks.sh will prompt you to enter tracks (as lowercase eg rpb, bc, bci) and positions
  - data will be written to a .txt file generated in src/
- update_data.sh will automatically generate cumulative point average plots (over time) for every track
  - data will be written to a folder called tracks_over_time
  - a ranking of tracks by average points will be output to terminal
  - (WIP) update_data.sh hist will create a histogram of track averages.

## Project Structure

```bash
├── enter_tracks.sh  
├── update_data.sh  
└── src  
    ├── placement_store.cpp  
    ├── visualization.py  
    └── tracks.h  
```
