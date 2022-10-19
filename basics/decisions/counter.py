"""
Counting the number of odd/even numbers entered by the user
"""

number_one = input("Please enter the first whole number.\n")
number_two = input("Please enter the second whole number.\n")
number_three = input("Please enter the third whole number.\n")

number_of_odds = 0
number_of_evens = 0
if (number_one % 2) == 0:
    number_of_evens += 1
else:
    number_of_odds += 1
if (number_two % 2) == 0:
    number_of_evens += 1
else:
    number_of_odds += 1
if (number_three % 2) == 0:
    number_of_evens += 1
else:
    number_of_odds += 1
