from datetime import datetime

def get_longest_streak(habits):
    """
    Finds the habit with the longest consecutive streak while respecting the periodicity.
    Args:
        habits (dict): The dictionary storing all habits.
    Returns:
        tuple: (habit name, longest streak count)
    """

    # Variables to track the habit with the longest streak
    max_streak = 0
    longest_habit = None

    # Loop through all habits in the tracker
    for habit, details in habits.items():

        # Skip habits that have no recorded completions
        if not details["completions"]:
            continue

        # Sort completion dates in ascending order
        completions = sorted(details["completions"])

        streak = 1  # Start streak count at 1 (since the habit has at least one completion)

        # Go through each completion and compare it with the previous one
        for i in range(1, len(completions)):
            prev_date = datetime.fromisoformat(completions[i - 1])  # Previous completion date
            curr_date = datetime.fromisoformat(completions[i])  # Current completion date
            delta = (curr_date - prev_date).days  # Difference in days between two completions

            # Check periodicity type and verify if habit was completed on time
            if details["periodicity"] == "daily" and delta == 1:
                streak += 1  # Increase streak if completed daily without missing a day
            elif details["periodicity"] == "weekly" and delta == 7:
                streak += 1  # Increase streak if completed exactly 7 days apart
            elif details["periodicity"] == "monthly":
                # Check if the month changed correctly (handles different month lengths)
                if prev_date.month != curr_date.month and curr_date.day >= prev_date.day:
                    streak += 1  # Increase streak if completed in consecutive months
            else:
                streak = 1  # Reset streak if the habit was not completed on time

        # Update max_streak if a new longest streak is found
        if streak > max_streak:
            max_streak = streak
            longest_habit = habit

    return longest_habit, max_streak
