"""Demonstrates simple while loop."""

number_of_cables = int(input("How many cables should I remove?\n"))
print()
while number_of_cables > 0:
    print("Cable removed.")
    number_of_cables -= 1
