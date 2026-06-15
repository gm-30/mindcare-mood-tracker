
import pandas as pd
from insights import generate_ai_insights

def generate_report():
    try:
        moods = pd.read_csv(
            "data/moods.csv",
            names=["date", "score", "label", "notes"]
        )

        sleep = pd.read_csv(
            "data/sleep.csv",
            names=["date", "hours", "quality"]
        )

        avg_mood = moods["score"].astype(float).mean()
        avg_sleep = sleep["hours"].astype(float).mean()

        print("\n=== WELLBEING REPORT ===")
        print(f"Average Mood: {avg_mood:.2f}/5")
        print(f"Average Sleep: {avg_sleep:.2f} hours")

        for insight in generate_ai_insights(avg_mood, avg_sleep):
            print("-", insight)

    except FileNotFoundError:
        print("No data available yet.")
    except Exception as e:
        print("Unable to generate report:", e)
