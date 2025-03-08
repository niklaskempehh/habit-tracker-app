def add_habit(habits):
    """Allows user to add a new habit with valid periodicity (daily/weekly/monthly only)."""
    name = input("Enter habit name: ")
    # Check if habit already exists before asking for periodicity
    if name in habits:
        print("This habit already exists!")
        return  # Exit the function early

    # Ask for valid periodicity only if habit is new
    while True:
        periodicity = input("Enter periodicity (daily/weekly/monthly): ").strip().lower()
        if periodicity in ["daily", "weekly", "monthly"]:
            break  # Exit loop if input is valid
        else:
            print("Invalid input. Please enter 'daily', 'weekly', or 'monthly'.")

    # If habit is new and periodicity is valid, add it
    habits[name] = {"periodicity": periodicity, "completions": []}
    print(f"Habit '{name}' added with periodicity: {periodicity}")

def complete_habit(habits):
    """Marks a habit as completed."""
    name = input("Enter the habit's name you wish to mark as complete: ")

    if name in habits:
        import datetime
        timestamp = datetime.datetime.now().isoformat()
        habits[name]["completions"].append(timestamp)
        print(f"'{name}' marked as completed on {timestamp}")
    else:
        print("This habit could not be found.")

def view_habits(habits):
    """Displays all tracked habits."""
    if not habits:
        print("No habits found.")
    else:
        for name, details in habits.items():
            print(f"- {name} ({details['periodicity']}): {len(details['completions'])} completions")
