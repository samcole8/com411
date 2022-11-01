"""Playing around with lists."""


def movements():
    """Return a string."""
    path = ["Move Forward",
            10,
            "Move Backward",
            5,
            "Move Left",
            3,
            "Move Right",
            1]
    return path


def run():
    """Run the program."""
    print("Moving...")
    for i in range(0, len(movements()), 2):
        direction = movements()[i]
        steps = movements()[i+1]
        print(f"{direction} for {steps} steps")


if __name__ == "__main__":
    run()
