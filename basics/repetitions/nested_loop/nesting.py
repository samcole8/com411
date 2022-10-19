"""
Awful, overcomplicated script to calculate the distance between two unique
identical characters in a given string.
"""

# Take input for string and marker characters
string = input("Please enter a sequence\n")
marker = input("Please enter the character for the marker\n")
# Initialise count to count distance
count = 0

for character_index in range(0, len(string)):
    if string[character_index] == marker:
        for nested_character_index in range((character_index + 1), len(string)):
            if string[nested_character_index] == marker:
                print(f"\nThe distance between the markers is {count}.")
            else:
                count += 1
