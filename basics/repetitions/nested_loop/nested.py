"""An example of nested for loops."""

ASCII_emoji = ":-) "  # pylint: disable-msg=C0103
number_of_rows = int(input("How many rows should I have?\n"))
number_of_columns = int(input("How many columns should I have?\n"))
print("Here I go:\n")
for row in range(0, number_of_rows):
    for column in range(0, number_of_columns):
        print(ASCII_emoji, end="")
    print()
