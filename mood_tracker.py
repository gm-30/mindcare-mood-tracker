
import csv
from datetime import date

MOODS = {
    "1": "Very Stressed",
    "2": "Sad",
    "3": "Neutral",
    "4": "Happy",
    "5": "Very Happy"
}

def log_mood():
    score = input("Mood score (1-5): ")

    if score not in MOODS:
        print("Invalid mood.")
        return

    notes = input("Notes (optional): ")

    with open("data/moods.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([str(date.today()), score, MOODS[score], notes])

    print("Mood recorded!")
