"""Use modulo operator to determine whether a number is odd or even."""

number = int(input("Please enter a whole number:\n"))
if (number % 2) == 0:
    print(f"\nThe number {number} is an even number.")
else:
    print(f"\nThe number {number} is an odd number.")
