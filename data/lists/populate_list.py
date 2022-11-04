"""Populate a list."""


def directions():
    """Return list of directions."""
    direction_list = ["Move Forward",
                      "Move Backward",
                      "Turn Left",
                      "Turn Right"]
    return direction_list


def menu():
    """Display contents of list."""
    direction_list = directions()
    print("Please select a direction: ")
    # Display menu
    for index in range(len(direction_list)):
        print(f"{index}: {direction_list[index]}")
    choice = int(input("\n"))
    return direction_list[choice]


def run():
    """Run the program."""
    route = []
    print("Working out escape route...")
    for _i in range(5):
        route.append(menu())
    print(f"Escape route: {route}")


if __name__ == "__main__":
    run()
