
import os, csv
from mood_tracker import log_mood
from sleep_tracker import log_sleep
from journal import add_journal
from analytics import generate_report
from calendar_view import show_calendar

def menu():
    while True:
        print("\n=== MindCare ===")
        print("1. Record Mood")
        print("2. Log Sleep")
        print("3. Journal Entry")
        print("4. View Mood Calendar")
        print("5. Weekly Insights")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            log_mood()
        elif choice == "2":
            log_sleep()
        elif choice == "3":
            add_journal()
        elif choice == "4":
            show_calendar()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("Take care!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
