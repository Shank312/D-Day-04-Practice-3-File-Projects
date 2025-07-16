# 📁 Practice 3 – Python File Projects

This repository contains three beginner-friendly Python projects that focus on **file handling**, **user interaction**, and **text processing**. These mini-apps are fully functional and run directly in the command line. Each project demonstrates real-world applications of reading, writing, and manipulating files.

---

## 📝 Project 01 – Daily Journal Logger

A simple CLI application to help you log daily thoughts, goals, or reflections.

### ✅ Features:
- Prompts user to enter a journal entry.
- Saves entries with the **current date** as a header.
- Appends each entry to a persistent `journal.txt` file.
- Allows viewing all previous journal entries.
- Uses `datetime` and `os` for managing entries.

### 📌 Sample Output:
Daily Journal Logger

Write a new entry.

Read all entries.

Exit.
Choose an option (1-3): 2

Journal Entries:

[2025-07-15]
I woke up at 8 O' Clock in morning...

[2025-07-15]
Now it is evening and time is 6:00 pm...


---

## 👥 Project 02 – Contact Book App

A basic contact management system where users can store, view, and search for contact details.

### ✅ Features:
- Add new contacts with name, phone number, and email.
- View all saved contacts.
- Search for contacts by name (case-insensitive).
- Stores contacts in a simple CSV-like format (`contacts.txt`).
- Handles file creation and reading via `os.path.exists()`.

### 📌 Sample Output:
Contact Book

Add a contact

View all contacts

Search for contact

Exit
Choice an option (1-4): 2

Contacts:
Name: Shankar Kumar, Phone: 7289072476, Email: shankark3121999@gmail.com
Name: Suraj Kumar, Phone: 7538356383, Email: surajkumar@gmail.com


---

## 📄 Project 03 – Read and Summarize a Text File

A text summarizer that extracts the **most important sentences** from a given `.txt` file and provides a basic statistical overview.

### ✅ Features:
- Accepts a file path as input.
- Cleans and preprocesses text using regex and `collections.Counter`.
- Summarizes the content by scoring and selecting top sentences.
- Handles missing or unreadable files gracefully.

### 📌 Sample Input File (`sample.txt`):
> The rapid advancement of artificial intelligence has ignited discussions...  
> In the healthcare sector, AI algorithms are being used...  
> Elon Musk and other tech leaders have voiced concerns...

### 📌 Sample Output:
Enter the path to the text file: sample.txt

Summary:
The rapid advancement of artificial intelligence has ignited discussions across various sectors...
Elon Musk and other tech leaders have voiced concerns...
Collaborative international frameworks and ethical AI development can unlock tremendous potential...


---

## 🧠 Skills and Concepts Covered

- Python `open()`, `read()`, `write()`, `append()` modes
- Using `with` block for safe file handling
- Basic string manipulation and formatting
- Data preprocessing using `re` and `collections.Counter`
- Handling missing files with `try-except`
- Menu-driven command-line interface

---

## 🗂️ Folder Structure

Practice 3 File Projects/
├── Project 01 - Daily Logger/
│ └── daily_journal_logger.py
├── Project 02 - Contact Book App/
│ └── contact_book.py
├── Project 03 - Read and Summarize a Text File/
│ └── text_summarizer.py
├── sample.txt
└── README.md


---

## 🏁 How to Run

1. Make sure Python 3.10+ is installed on your system.
2. Clone or download the project folder.
3. Open a terminal in the respective project directory.
4. Run with:

```bash
python daily_journal_logger.py
python contact_book.py
python text_summarizer.py

💡 Author
Shankar Kumar
📧 shankark3121999@gmail.com
🔗 GitHub Profile
