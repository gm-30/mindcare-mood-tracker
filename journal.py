
import csv
from datetime import date

def add_journal():
    entry = input("How was your day? ")

    with open("data/journal.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([str(date.today()), entry])

    print("Journal saved!")
