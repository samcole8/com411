"""Simple script to reverse a string."""

forward_phrase = input("What phrase do you see?\n")
backward_phrase = ""  # pylint: disable-msg=C0103
print("\nReversing...")
for character in range(len(forward_phrase), 0, -1):
    backward_phrase += forward_phrase[character - 1]
print(f"\nThe phrase is: {backward_phrase}")
