"""Use min and max with tuple."""


def likelihood():
    """Create tuple."""
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run():
    """Run the program."""
    chance = likelihood()
    print(f"Minimum likelihood of falling {min(chance)}%")
    print(f"Maximum likelihood of falling {max(chance)}%")


if __name__ == "__main__":
    run()
