"""Docstring."""


def directions():
    """Return a string."""
    directions_list = ["Move Forward",
                       "Move Backward",
                       "Turn Left",
                       "Turn Right"]
    return directions_list


def run():
    """Run the program."""
    print(directions())


if __name__ == "__main__":
    run()
