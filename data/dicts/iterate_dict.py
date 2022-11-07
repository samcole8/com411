"""Create dictionary and variably iterate through."""


def pattern():
    """Create and return dictionary."""
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def display_keys(my_dictionary):
    """Iterate through and display keys from a dictionary."""
    for key in my_dictionary.keys():
        print(key)


def display_values(my_dictionary):
    """Iterate through and display values from a dictionary."""
    for value in my_dictionary.values():
        print(value)


def display_items(my_dictionary):
    """Iterate through and display keys and values from a dictionary."""
    for key, value in my_dictionary.items():
        print(f"{key}: {value}")


def run():
    """Run the program."""
    sequences = pattern()
    display_keys(sequences)
    display_values(sequences)
    display_items(sequences)


if __name__ == "__main__":
    run()
