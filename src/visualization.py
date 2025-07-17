#data visualization!!
import pandas as pd # type: ignore
import os
from datetime import datetime
import matplotlib.pyplot as plt # type: ignore
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "position_data.txt")

def load_data():
    df = pd.read_csv(DATA_FILE, names=["Track", "Position"])
    df["Position"] = pd.to_numeric(df["Position"], errors='coerce')
    return df.dropna()

def plot_histogram(df):
    avg_positions = df.groupby("Track")["Position"].mean().sort_values()

    # Create plot
    plt.figure(figsize=(10, 8))
    avg_positions.plot(kind='barh', color='skyblue')
    plt.xlabel("Average Position")
    plt.title("Average Placement per Track")
    plt.tight_layout()

    # Prepare output directory and timestamped filename
    output_dir = "average_histograms"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"average_placements_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)

    # Save to file
    plt.savefig(filepath)
    plt.close()  # Prevent re-showing in case of loops

    print(f"Histogram saved as: {filepath}")

def pos_to_points(pos):
    if (pos == 1):
        return 15
    elif (pos == 2):
        return 12
    return 13-pos

def print_ranking(df):
    stats = (
    df.groupby("Track")["Position"]
      .apply(lambda positions: positions.apply(pos_to_points).mean())
      .to_frame(name="mean")
    )

    # Add count column
    stats["count"] = df.groupby("Track")["Position"].count()

    # Sort by average points
    stats = stats.sort_values("mean", ascending=False)

    print("\nTrack Rankings (by Avg Points):\n")
    for i, (track, row) in enumerate(stats.iterrows(), 1):
        avg = row["mean"]
        count = row["count"]
        print(f"{i:2}. {track:<10} Avg Points: {avg:.2f} ({int(count)} instances)")

def plot_track_over_time(df, track_name):
    track_df = df[df["Track"].str.lower() == track_name.lower()]
    if track_df.empty:
        print(f"No data found for track: {track_name}")
        return
    
    track_df = track_df.reset_index(drop=True)
    track_df["Race Number"] = track_df.index + 1

    # Convert Position to Points
    track_df["Points"] = track_df["Position"].apply(pos_to_points)
    # Compute cumulative (running) average
    track_df["Running Avg Points"] = track_df["Points"].expanding().mean()

    plt.plot(track_df["Race Number"], track_df["Running Avg Points"], marker='o')
    plt.title(f"Points Over Time: {track_name}")
    plt.xlabel("Race Number")
    plt.ylabel("Cumulative Average Points")
    plt.grid(True)
    plt.tight_layout()
    
    # Prepare output directory and timestamped filename
    output_dir = "tracks_over_time"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{track_name}.png"
    filepath = os.path.join(output_dir, filename)

    if os.path.exists(f"tracks_over_time/{filename}"):
        os.remove(f"tracks_over_time/{filename}")
        print(f"Updating history for {track_name}")

    # Save to file
    plt.savefig(filepath)
    plt.close()  # Prevent re-showing in case of loops

def update_all_track_plots(df):
    unique_tracks = df["Track"].dropna().unique()
    print(f"Updating {len(unique_tracks)} track plots...")

    for track in unique_tracks:
        plot_track_over_time(df, track)

    print("All track plots updated.")
    


def main():
    df = load_data()
    update_all_track_plots(df)
    print_ranking(df)

    if len(sys.argv) > 1 and sys.argv[1].lower() == "hist":
        plot_histogram(df)
    if len(sys.argv) > 1 and sys.argv[1].lower() == "his":
        print('SHUT UP U STUPID BIATCH.')


    sys.exit()

if __name__ == "__main__":
    main()










