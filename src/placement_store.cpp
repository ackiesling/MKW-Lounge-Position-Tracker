#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
#include "tracks.h"

const std::string DATA_FILE = "src/position_data.txt";

struct TrackEntry {
    std::string track;
    int placement;

    std::string toString() const {
        return track + ", " + std::to_string(placement);
    }

    static TrackEntry fromString(const std::string& line) {
        std::istringstream iss(line);
        std::string track;
        int placement;
        std:getline(iss, track, ',');
        iss >> placement;
        return {track, placement};
    }
};

//load track entries

std::vector<TrackEntry> loadData() {
    std::vector<TrackEntry> entries;
    std::ifstream file(DATA_FILE);
    std::string line;
    while (std::getline(file, line)) {
        entries.push_back(TrackEntry::fromString(line));
    }
    return entries;
}

//save entries to file

void saveData(const std::vector<TrackEntry>& entries) {
    std::ofstream file(DATA_FILE);
    for (const auto& entry : entries) {
        file << entry.toString() << "\n";
    }
}

bool isValidTrack(const std::string& track) {
    for (const std::string& t : TRACK_NAMES) {
        if (t == track) return true;
    }
    return false;
}

int main() {
    std::vector<TrackEntry> history = loadData();

    std::cout << "MKW Lounge Position Tracker\n";
    std::cout << "Enter track name and placement (1-12) or type 'back' to undo.\n";

    while (true) {
        std::string input;
        std::cout << "\nTrack name: ";
        std::getline(std::cin, input);

        if (input == "back") {
            if (!history.empty()) {
                history.pop_back();
                saveData(history);
                std::cout << "Last entry removed.";
            } else {
                std::cout << "No entries to undo.";
            }
            continue;
        }

        if (!isValidTrack(input)) {
            std::cout << "Invalid track name. Try again.";
            continue;
        }

        std::string placementStr;
        int placement;
        std::cout << "Placement (1-12): ";
        std::getline(std::cin, placementStr);
        try {
            placement = std::stoi(placementStr);
            if (placement < 1 || placement > 12) {
                throw std::out_of_range("Out of range");
            }
        } catch (...) {
            std::cout << "Invalid placement. Try again.";
            continue;
        }

        history.push_back({input,placement});
        saveData(history);
        std::cout << "Entry saved.";
    }
    return 0;
}

