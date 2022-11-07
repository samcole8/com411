"""Demonstrates nested dictionaries."""


def short_pattern():
    """Create a short dictionary."""
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern


def medium_pattern():
    """Create a medium dictionary."""
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern


def long_pattern():
    """Create a long dictionary."""
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern


def run():
    """Run the program."""
    print("Analysing patterns...")
    # Create nested dictionary
    pattern_dict = {
                    "short sequence": short_pattern(),
                    "medium sequence": medium_pattern(),
                    "long sequence": long_pattern(),
                    }
    # Display contents of pattern_dict
    for key, value in pattern_dict.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    run()
