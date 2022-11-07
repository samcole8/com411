"""Code demonstrating how to sort a set."""


def observed():
    """Return set."""
    observations = []
    # Create list from user input
    for _i in range(5):
        user_input = input("Please enter an observation:  ")
        observations.append(user_input)
    return observations


def remove_observations(observation_list):
    """Remove object from a list."""
    # Loop until user quits
    loop_on = True
    while loop_on:
        # Branch by user input
        user_input = input("\nDo you wish to remove observations? [Y/n]: ")
        if user_input in ("y", "", "Y"):
            # Remove item from list
            user_input = input("What observation do you wish to remove?")
            observation_list.remove(user_input)
            print(f"Removed {user_input} from the list.")
        else:
            # Exit loop
            print()
            loop_on = False


def run():
    """Run the program."""
    # Create list and allow user to remove items.
    observation_list = observed()
    remove_observations(observation_list)
    # Create set
    observation_set = set()
    # Add each item, and the number of times it appears to the set as a tuple.
    for value in observation_list:
        value_count = observation_list.count(value)
        observation_set.add((value, value_count))
    # Output contents of set
    print("Observations:")
    observation_set = sorted(observation_set)
    for value in observation_set:
        print(f"{value[0]} was observed {value[1]} times.")


if __name__ == "__main__":
    run()
