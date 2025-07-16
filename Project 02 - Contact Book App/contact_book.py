
''' 🧠 Objective: Store and retrieve contact info (Name, Phone, Email).

🔧 Features:
Add new contacts.

View all saved contacts.

Stores data in a text file line-by-line or as CSV.

💡 Concepts Used:
Menu-driven app (input() with options)

File open() in append/read mode

split() and .strip() for formatting
'''

import os

def add_contact():
    contact_file = "contacts.txt"
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter Email: ")
    with open(contact_file, "a") as file:
        file.write(f"{name}, {phone}, {email}\n")
    print("Conatct added successfully!")

def view_contacts():
    conatct_file = "contacts.txt"
    if os.path.exists(conatct_file):
        with open(conatct_file, "r") as file:
            print("\nContacts: ")
            for line in file:
                name, phone, email = line.strip().split(",")
                print(f"Name: {name}, Phone: {phone}, Email: {email}")
    else:
        print("No contact found.")

def search_contact():
    contact_file = "contacts.txt"
    search_name = input("Enter name to search: ").lower()
    if os.path.exists(contact_file):
        with open(contact_file, "r") as file:
            found = False                                    # initially assumed faise
            for line in file:
                name, phone, email = line.strip().split(",")
                if search_name in name.lower():
                    print(f"Found: Name: {name}, Phone: {phone}, Email: {email}")
                    found = True
            if not found:
                print("No matching contacts found.")
    else:
        print("No contacts found.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search for contact")
        print("4. Exit")
        choice = input("Choice an option (1-4): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()




