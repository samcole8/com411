"""Simple script demonstrating a function with a nested decision statement."""


def identify():
    """Take user input."""
    seen = input("What lies before us? \n")
    if seen == "a large boulder":
        print("\nIt's time to run!")
    else:
        print("\nWe will be fine.")


identify()
