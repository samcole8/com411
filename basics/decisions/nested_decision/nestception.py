"""Demonstrates multiple nested if statements."""

user_input = input("Where should I look?\n")
if user_input == "in the bedroom":
    if input("Where in the bathroom should I look?\n") == "under the bed":
        print("Found some shoes but no battery.")
    else:
        print("Found some mess but no battery.")
elif user_input == "in the bathroom":
    if input("Where in the bathroom should I look\n") == "in the bathtub":
        print("Found a rubber duck but no battery.")
    else:
        print("Found a wet surface but no battery.")
elif user_input == "in the lab":
    if input("Where in the lab should I look?\n") == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
