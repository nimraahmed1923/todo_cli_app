import json
from datetime import date

# ========================
# STUDY TRACKER
# by Nimra Ahmed
# ========================

def load_log():
    try:
        with open('study_log.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_log(log):
    with open('study_log.json', 'w') as f:
        json.dump(log, f, indent=4)

def add_entry(log):
    subject = input("Subject studied: ")
    hours = float(input("Hours studied: "))
    entry = {
        "date": str(date.today()),
        "subject": subject,
        "hours": hours
    }
    log.append(entry)
    save_log(log)
    print(f"✅ Saved! {subject} for {hours} hours!")

def view_log(log):
    if not log:
        print("No entries yet!")
        return
    print("\n=== STUDY LOG ===")
    total = 0
    for entry in log:
        print(f"{entry['date']} | "
              f"{entry['subject']} | "
              f"{entry['hours']} hours")
        total += entry['hours']
    print(f"\nTotal hours studied: {total}! 🎉")

def main():
    log = load_log()
    while True:
        print("\n=== STUDY TRACKER ===")
        print("1. Add study entry")
        print("2. View study log")
        print("3. Exit")
        choice = input("Choice (1-3): ")

        if choice == "1":
            add_entry(log)
        elif choice == "2":
            view_log(log)
        elif choice == "3":
            print("Keep studying Nimmi! 💪")
            break
        else:
            print("Invalid choice!")

main()