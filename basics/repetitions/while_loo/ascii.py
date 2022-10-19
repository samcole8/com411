"""
Demonstrates the implementation of counting with while loops
"""

number_of_bars = int(input("How many bars should be charged?\n"))
count = 0 # pylint: disable-msg=C0103
print()
while count < number_of_bars:
    count += 1
    print("|" * count)
print("\nThe battery is fully charged.")
