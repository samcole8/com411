"""Use min with tuple."""


def likelihood():
    """Create tuple."""
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run():
    """Run the program."""
    print(f"Minimum likelihood of falling {likelihood()}%")


if __name__ == "__main__":
    run()
