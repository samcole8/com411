"""Script to reverse a string using membership operators."""

forward_phrase = input("What phrase do you see?\n")
print("\nReversing")
backward_phrase = ""  # pylint: disable-msg=C0103
for character in forward_phrase:
    backward_phrase = character + backward_phrase
print(f"\nThe phrase is {backward_phrase}")
