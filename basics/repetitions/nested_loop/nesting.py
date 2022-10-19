"""
Script to calculate the distance between two characters
NEEDS WORK
"""

sequence = input("Please enter a sequence:\n")
marker = input("Please enter the marker character\n")
index_1 = 0
index_2 = 0
for index in range(0, len(sequence)):
    if (sequence[index] == marker):
        if index_1 == 0:
            index_1 = index
        else:
            index_2 = index
print(f"\nThe markers are {(index_2 - index_1 - 1)} characters apart.")

