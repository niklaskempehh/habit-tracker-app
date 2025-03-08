import json

def save_data(data, filename="habits.json"):
    """Saves habit data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_data(filename="habits.json"):
    """Loads habit data from a JSON file. If file does not exist, returns an empty dictionary."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}