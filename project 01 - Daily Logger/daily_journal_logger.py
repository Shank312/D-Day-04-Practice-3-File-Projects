
''' 🧠 Objective: Log daily thoughts or goals into a dated text file automatically.

🔧 Features:
Asks user to input today’s journal entry.

Automatically creates a file named with today’s date.

Appends new entries if the file already exists.

Includes a timestamp with each entry.

💡 Concepts Used:
datetime module

File open() in append mode ('a')

with statement
'''

import datetime
import os

def write_journal_entry():
    journal_file = "journal.txt"
    today = datetime.datetime.now().strftime("%Y-%m-%d")             # module_name.ClassName.CallingFunction
    entry = input("Enter your journal entry for today: ")
    with open(journal_file, "a") as file:
        file.write(f"\n[{today}]\n{entry}\n")
    print("Entry saved successfully!")

def read_journal():
    journal_file = "journal.txt"
    if os.path.exists(journal_file):
        with open(journal_file, "r") as file:
            print("\nJournal Entries: ")
            print(file.read())
    else:
        print("No journal entries found.")

def main():
    while True:
        print("\nDaily Journal Logger")
        print("1. Write a new entry.")
        print("2. Read all entries.")
        print("3. Exit.")
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            write_journal_entry()
        elif choice == "2":
            read_journal()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


