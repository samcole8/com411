"""Use min and max with tuple."""


def steps():
    """Create tuple."""
    likelihoods = [("step 1", 50),
                   ("step 2", 38),
                   ("step 3", 27),
                   ("step 4", 99),
                   ("step 5", 4)]
    return likelihoods


def run():
    """Run the program."""
    good_steps = 0
    bad_steps = 0
    for step in steps():
        if step[1] >= 50:
            good_steps += 1
        else:
            bad_steps += 1
    print(f"Good steps: {good_steps}, Bad steps: {bad_steps}")


if __name__ == "__main__":
    run()
