"""
Simple script to calculate the sum of the first 100 numbers.
"""

print("Calculating the sum of the first 100 numbers...")
number = 100 # pylint: disable-msg=C0103
sum_of_numbers = 0 # pylint: disable-msg=C0103
while number > 0:
    sum_of_numbers += number
    number -= 1
print(f"...Done! The answer is {sum_of_numbers}.")
