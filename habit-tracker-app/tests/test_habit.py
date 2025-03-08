from habit_tracker.habit_manager import add_habit, complete_habit
from unittest.mock import patch

# Create an empty habit dictionary (simulating stored habits)
def test_add_habit():
    """Test adding a new habit."""
    habits = {}  # Reset dictionary for each test
    with patch("builtins.input", side_effect=["Drink Water", "daily"]):
        add_habit(habits)

    assert "Drink Water" in habits
    assert habits["Drink Water"]["periodicity"] == "daily"

def test_duplicate_habit():
    """Test adding a duplicate habit."""
    habits = {"Drink Water": {"periodicity": "daily", "completions": []}}
    with patch("builtins.input", side_effect=["Drink Water", "daily"]):
        add_habit(habits)

    assert len(habits) == 1  # The habit should not be added twice

def test_complete_habit():
    """Test completing a habit."""
    habits = {"Drink Water": {"periodicity": "daily", "completions": []}}
    with patch("builtins.input", side_effect=["Drink Water"]):
        complete_habit(habits)

    assert len(habits["Drink Water"]["completions"]) == 1

def test_complete_non_existing_habit():
    """Test completing a non-existing habit (should fail)."""
    habits = {"Drink Water": {"periodicity": "daily", "completions": []}}
    with patch("builtins.input", side_effect=["Exercise"]):
        complete_habit(habits)  # This should not add a completion

    assert "Exercise" not in habits