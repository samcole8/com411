"""Script to calculate to factorial (x!) of number x."""

x = int(input("Please enter a number:\n"))
factorial = 1  # pylint: disable-msg=C0103
while x > 0:
    factorial *= x
    x -= 1
print(f"\nThe factorial is {factorial}.")
