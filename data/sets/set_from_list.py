"""Code demonstrating use of tuples in a set."""


def observed():
    """Return set."""
    observations = []
    # Create list from user input
    for _i in range(7):
        user_input = int(input("Please enter an observation:  "))
        observations.append(user_input)
    return observations


def run():
    """Run the program."""
    print("Counting observations...")
    # Create populated list and set.
    observation_set = set()
    observation_list = observed()
    # Add each item, and the number of times it appears to the set as a tuple.
    for value in observation_list:
        value_count = observation_list.count(value)
        observation_set.add((value, value_count))
    # Output contents of set
    for value in observation_set:
        print(f"{value[0]} was observed {value[1]} times.")


if __name__ == "__main__":
    run()
