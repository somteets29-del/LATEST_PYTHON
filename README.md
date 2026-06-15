# LATEST_PYTHON 🐍

A collection of beginner Python projects built from scratch as part of my programming journey as a Computer Engineering student at FUTO. Each project tackles a real-world concept using only core Python — no external libraries.

---

## 📁 Repository Structure

```
LATEST_PYTHON/
│
├── School/
│   ├── cgpa_calculator.py
│   └── futo_rms.py
│
├── Games/
│   └── guessgame.py
│
├── Utilities/
│   └── atm_sim.py
│
└── inventory.py
```

---

## 📂 School

### 1. CGPA Calculator 📊

A command-line tool that calculates a student's semester CGPA based on courses, credit units, and grades using a 5-point grading scale. Results are saved to a text file.

**How to Run:**
```bash
python School/cgpa_calculator.py
```

**How it works:**
The program asks how many courses the student is taking, then collects the course name, credit unit, and grade for each one. It multiplies each credit unit by the grade point, sums them all up, and divides by the total credit units to get the CGPA. The result is then saved to a `.txt` file.

**Features:**
- Accepts both uppercase and lowercase grade input
- Restricts input to the exact number of courses specified
- Saves results to `cgpa_result.txt`

**Grade Scale:**
| Grade | Points |
|-------|--------|
| A     | 5      |
| B     | 4      |
| C     | 3      |
| D     | 2      |
| E     | 1      |
| F     | 0      |

---

### 2. FUTO Students Result Management System 🎓

An advanced result management tool that goes beyond CGPA calculation. It tracks grade distributions, lists all courses, displays a full result summary, and outputs the student's degree class.

**How to Run:**
```bash
python School/futo_rms.py
```

**How it works:**
The program collects course details the same way as the CGPA Calculator, but goes further — it counts how many A's, B's, and F's the student got, builds a full course result table, calculates the CGPA, and maps it to a degree class. Everything is displayed as a structured summary and saved to a file.

**Features:**
- Tracks number of A's, B's, and failed courses
- Displays full course list and result summary
- Outputs degree class (First Class, Second Class Upper, etc.)
- Saves results to a text file
- Limits input to a maximum of 20 courses

**Degree Class Scale:**
| CGPA        | Class              |
|-------------|--------------------|
| 4.50 - 5.00 | First Class        |
| 4.00 - 4.49 | Second Class Upper |
| 3.50 - 3.99 | Second Class Lower |
| 3.00 - 3.49 | Third Class        |
| Below 3.00  | Fail               |

---

## 📂 Games

### 3. Number Guessing Game 🎮

A fun interactive game where the computer picks a random number between 1 and 20 and the player tries to guess it, with hints after every attempt.

**How to Run:**
```bash
python Games/guessgame.py
```

**How it works:**
The program uses Python's `random` module to generate a number between 1 and 20. Each time the player guesses, the program checks if the guess is too high, too low, or correct. It keeps a count of every attempt and displays the total when the player wins.

**Features:**
- Random number generation
- Higher/Lower hints after each guess
- Tracks total number of attempts

---

## 📂 Utilities

### 4. FUTO Bank ATM Simulator 🏧

A simulated banking system that replicates basic ATM operations, secured with a PIN and account lockout after 3 failed attempts.

**How to Run:**
```bash
python Utilities/atm_sim.py
```

**How it works:**
The program starts by asking for a PIN. If the correct PIN is entered, the user gets access to a menu of banking operations. Each operation (deposit, withdrawal, transfer) updates the account balance and gives feedback. If the wrong PIN is entered 3 times, the account locks and the program exits.

**Features:**
- Check account balance
- Deposit funds
- Withdraw funds
- Transfer funds to another account
- PIN authentication with lockout after 3 failed attempts

---

## 📄 inventory.py

### 5. Library & Equipment Tracker 📦

A terminal-based inventory management system for tracking library resources and equipment. Items can be borrowed, returned, and searched, with real-time status updates.

**How to Run:**
```bash
python inventory.py
```

**How it works:**
The inventory is stored as a list of lists, where each item has a name and a status (`Available` or `Borrowed`). The program runs a menu loop where the user can view, search, borrow, return, or add items. Each action calls a dedicated function that searches through the list, checks the item's status, and updates it accordingly. All comparisons are case-insensitive to handle varied user input.

**Features:**
- View all currently available items
- Search for items by keyword
- Borrow items and mark them as unavailable
- Return items and restore their availability
- Add new items to the inventory
- Clear feedback messages for all actions

---

### 6. 💸 Expense Tracker (CLI)

A command-line expense management system built with Python. This project allows users to add, view, update, delete, and summarize expenses — all from the terminal.

---

## 🚀 Features

- Add new expenses with month, description, and amount
- View all recorded expenses in a formatted list
- Update existing expenses by ID
- Delete expenses by ID
- View total expenses across all months
- View a monthly expense summary

---

---

## 📸 How It Works

The program runs a menu-driven loop where the user selects an action:

```
1. View Expenses
2. Add Expenses
3. Delete Expenses
4. Update Expenses
5. View Total Expenses
6. Monthly Summary
7. Exit
```

Each expense is stored as:
```python
[ID, Month, Description, Amount]
```

---

---

## ▶️ How to Run

```bash
python expense_tracker.py
```

> Tested on Python 3.x via Termux (Android) and Pydroid 3.

---

## 📁 Project Structure

```
expense_tracker/
└── expense_tracker.py
```

---

## 🔮 Future Improvements

- Save expenses to a file (CSV or JSON) for persistence
- Input validation and error handling for invalid entries
- Filter expenses by description keyword
- Export monthly summary as a report

---

## ⚙️ Requirements
- Python 3.x
- No external libraries needed

---

## 👤 Author
**Somto** — Computer Engineering Student, Federal University of Technology Owerri (FUTO)
