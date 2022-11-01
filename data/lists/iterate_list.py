"""Iterate through string."""


def directions():
    """Return a list."""
    directions_list = ["Move Forward",
                       "Move Backward",
                       "Turn Left",
                       "Turn Right"]
    return directions_list


def menu():
    """Output list of directions."""
    print("Please select a direction:")
    directions_list = directions()
    for index in range(len(directions_list)):
        direction = directions_list[index]
        print(f"{index}: {direction}")


def run():
    """Run the program."""
    menu()


if __name__ == "__main__":
    run()
