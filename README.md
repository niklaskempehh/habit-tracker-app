# 📌 **Habit Tracker App**

A Simple CLI-Based Habit Tracking System

## 📝 Table of Contents

* 	Overview
* 	Features
* 	Project Structure
* 	Installation
* 	Usage
* 	Analytics & Habit Tracking
* 	Running Tests

⸻

## 📌 Overview

The Habit Tracker App is a command-line interface (CLI) tool that helps users build and maintain good habits by tracking them on a daily, weekly, or monthly basis. The app provides functionalities to add, complete, and analyze habits while storing the data in a simple JSON file.

This project follows a modular structure, ensuring maintainability and scalability.

⸻

## ✨ Features

* Add new habits with a specific periodicity (daily, weekly, monthly)
* Mark habits as completed with automatic timestamps 
* ️View all tracked habits and their completion counts 
* Analyze progress and identify the longest streak 
* Persistent data storage using JSON 
* Simple and intuitive command-line interface (CLI)

⸻

## 📂 Project Structure

```habit-tracker-app/
│── habit_tracker/         # Main application package
│   ├── __init__.py        # Makes the folder a package
│   ├── main.py            # Core CLI application
│   ├── habit_manager.py   # Handles habit CRUD operations
│   ├── data_handler.py    # JSON data management
│   ├── analytics.py       # Habit analysis functions
│── tests/                 # Unit tests for validation
│   ├── test_habit.py      # Habit management tests
│   ├── test_streak.py     # Streak calculation tests
│── .gitignore             # Ignore unnecessary files
│── README.md              # Project documentation
│── requirements.txt       # Dependencies
│── habits.json            # Sample habit data
```

⸻

## ⚙️ Installation

To set up the project on your local machine:

1️⃣ Clone the Repository
```
git clone https://github.com/niklaskempehh/habit-tracker-app.git
cd habit-tracker-app
```

2️⃣ Create & Activate a Virtual Environment
```
python -m venv .venv
source .venv/bin/activate  # (Windows users: .venv\Scripts\activate)
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

⸻

## 🚀 Usage
Once installed, you can start the Habit Tracker App:
```
python -m habit_tracker.main
```

Main Menu
```
HABIT TRACKER MENU

1. Add a new habit
2. Complete a habit
3. View all habits
4. View longest streak
5. Exit

Choose an option (1, 2, 3, 4, or 5):
```

1️⃣ Add a Habit
```
Enter habit name: Drink Water
Enter periodicity (daily/weekly/monthly): daily
Habit 'Drink Water' added with periodicity: daily
```

2️⃣ Complete a Habit
```
Enter the habit's name you wish to mark as complete: Drink Water
'Drink Water' marked as completed on 2025-03-01T08:00:00
```

3️⃣ View All Habits
```
Tracked Habits:
- Drink Water (daily): 3 completions
- Exercise (weekly): 1 completion
```

4️⃣ View Longest Streak
```
The habit with the longest streak is 'Drink Water' with 28 completions!
```

5️⃣ Exit
```
Goodbye!
```

⸻

## 📊 Analytics & Habit Tracking
The analytics module (analytics.py) provides habit insights:
* get_longest_streak(habits): Finds the habit with the most consecutive 
