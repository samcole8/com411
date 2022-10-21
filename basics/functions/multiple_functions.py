"""Code demonstrating multiple functions."""


def display_ladder(steps):
    """Print a string based on the parameter."""
    for _i in range(0, steps):
        print("| |")
        print("***")


def create_ladder():
    """Take input for steps and call function."""
    steps = int(input("How many steps remain?"))
    display_ladder(steps)


create_ladder()
