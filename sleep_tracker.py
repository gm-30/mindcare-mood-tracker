
import csv
from datetime import date

def log_sleep():
    hours = input("Hours slept: ")
    quality = input("Quality (Poor/Fair/Good): ")

    with open("data/sleep.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([str(date.today()), hours, quality])

    print("Sleep logged!")
