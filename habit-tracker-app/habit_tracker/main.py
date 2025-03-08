from habit_manager import add_habit, complete_habit, view_habits
from data_handler import load_data, save_data
from analytics import get_longest_streak

def menu():
    """
    Displays the habit-tracker-app menu.
    """
    habits = load_data()

    while True:
        print("\n HABIT TRACKER MENU")
        print("\n1. Add a new habit")
        print("2. Complete a habit")
        print("3. View all habits")
        print("4. View longest streak")
        print("5. Exit")

        choice = input("\nChoose an option (1, 2, 3, 4, or 5): ")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            complete_habit(habits)
        elif choice == "3":
            view_habits(habits)
        elif choice == "4":
            habit, streak = get_longest_streak(habits)
            if habit:
                print(f"\nThe habit with the longest streak is '{habit}' with {streak} completions!")
            else:
                print("\nNo habits found.")
        elif choice == "5":
            save_data(habits)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# This ensures that the menu() function only runs if this script (main.py) is executed directly.
# If main.py is imported as a module into another script, menu() will not run automatically.
if __name__ == "__main__":
    menu()