"""Calculate distance between two unique identical characters in a string."""

# Take input for string and marker characters
string = input("Please enter a sequence\n")
marker = input("Please enter the character for the marker\n")
# Initialise count to count distance
count = 0  # pylint: disable-msg=C0103

for character_index in range(0, len(string)):
    if string[character_index] == marker:
        for char_index_2 in range((character_index + 1), len(string)):
            if string[char_index_2] == marker:
                print(f"\nThe distance between the markers is {count}.")
            else:
                count += 1
