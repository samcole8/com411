"""Script demonstrating multiple functions."""


def sum_weights(bot_weight_one, bot_weight_two):
    """Calculate the sum of two parameters."""
    print("The sum of Beep and Bop's weight is ")
    # Calculate sum and display on previous line
    print(f"{bot_weight_one + bot_weight_two}.", end="")


def calc_avg_weight(bot_weight_one, bot_weight_two):
    """Calculate the mean average of parameters."""
    print("Beep and Bop's mean weight is ")
    # Calculate mean and display on previous line
    print(f"{(bot_weight_one + bot_weight_two) / 2}.", end="")


def run():
    """Determine function to run and take inputs."""
    bot_weight_one = int(input("What is the weight of Beep? \n"))
    print()
    bot_weight_two = int(input("What is the weight of Bop? \n"))
    print()
    function = input("What would you like too calculate? (sum or average) \n")
    print()
    if function == "average":
        calc_avg_weight(bot_weight_one, bot_weight_two)
    elif function == "sum":
        sum_weights(bot_weight_one, bot_weight_two)
    else:
        print("Error: Invalid function")


run()
