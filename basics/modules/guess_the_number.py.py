"""Guess the number game."""

import random as rnd


def main():
    """Generate number and play game."""
    # Get mix/max values for random
    min_value = int(input("Enter the minimum value:\n"))
    max_value = int(input("Enter the maximum value:\n"))
    number = rnd.randint(min_value, max_value)  # Generate random number
    # Confirm to user
    print()
    print(f"I am thinking of a number between {min_value} and {max_value}")
    print("Can you guess what it is?")
    # Begin game
    game = "in progress"
    while game != "won":
        user_guess = int(input())
        # Display message based on comparison
        if user_guess > number:
            print("Your guess is too high!")
            print("Try again:")
        elif user_guess < number:
            print("Your guess is too low!")
            print("Try again:")
        else:
            game = "won"
            print("Congratulations! You guessed my number!")


main()
