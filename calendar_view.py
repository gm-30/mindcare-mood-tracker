
import pandas as pd

def show_calendar():
    try:
        moods = pd.read_csv(
            "data/moods.csv",
            names=["date", "score", "label", "notes"]
        )

        print("\n=== Mood History ===")

        for _, row in moods.iterrows():
            print(f"{row['date']} → {row['label']}")

    except FileNotFoundError:
        print("No mood entries found.")
