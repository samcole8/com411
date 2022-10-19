"""
Asks user how many numbers to take inputs for.
Takes inputs and adds them.
"""

number_of_numbers = int(input("How many numbers should I add?\n"))
print("")
sum_of_numbers = 0 # pylint: disable-msg=C0103
count = 1 # pylint: disable-msg=C0103
while count <= number_of_numbers:
    sum_of_numbers += int(input(
        f"Please enter number {count} of {number_of_numbers}:\n"
        ))
    count += 1
print(f"\nThe answer is {sum_of_numbers}.")
