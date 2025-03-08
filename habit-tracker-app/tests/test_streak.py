import pytest
from habit_tracker.analytics import get_longest_streak

# Sample habit data
@pytest.fixture
def sample_habits():
    return {
        "Drink Water": {
            "periodicity": "daily",
            "completions": [
                "2025-02-01T08:00:00", "2025-02-02T08:00:00", "2025-02-03T08:00:00",
                "2025-02-04T08:00:00", "2025-02-05T08:00:00", "2025-02-06T08:00:00",
                "2025-02-07T08:00:00", "2025-02-08T08:00:00", "2025-02-09T08:00:00",
                "2025-02-10T08:00:00", "2025-02-11T08:00:00", "2025-02-12T08:00:00",
                "2025-02-13T08:00:00", "2025-02-14T08:00:00", "2025-02-15T08:00:00",
                "2025-02-16T08:00:00", "2025-02-17T08:00:00", "2025-02-18T08:00:00",
                "2025-02-19T08:00:00", "2025-02-20T08:00:00", "2025-02-21T08:00:00",
                "2025-02-22T08:00:00", "2025-02-23T08:00:00", "2025-02-24T08:00:00",
                "2025-02-25T08:00:00", "2025-02-26T08:00:00", "2025-02-27T08:00:00",
                "2025-02-28T08:00:00"
            ]
        },
        "Exercise": {
            "periodicity": "weekly",
            "completions": [
                "2025-02-03T10:00:00", "2025-02-10T10:00:00",
                "2025-02-17T10:00:00", "2025-02-24T10:00:00"
            ]
        }
    }

def test_longest_streak(sample_habits):
    """Test longest streak calculation."""
    habit, streak = get_longest_streak(sample_habits)
    assert habit == "Drink Water"  # ✅ This should be the longest streak
    assert streak == 28  # ✅ Full 4-week streak