"""Program using functions to perform multiple operations on a word."""


def menu():
    """Display menu and choose function"""
    # Take input for word
    word = input("Please enter a word: \n")
    # Display menu
    print()
    print("Choose from the following options: \n")
    print("1) Display in a Box")
    print("2) Display Lower-case")
    print("3) Display Upper-case")
    print("4) Display Mirrored")
    print("5) Repeat")
    # Take input and call corresponding function
    function = input("\n")
    print()
    if function == "1":
        display_in_a_box(word)
    elif function == "2":
        display_lower_case(word)
    elif function == "3":
        display_upper_case(word)
    elif function == "4":
        display_mirrored(word)
    elif function == "5":
        display_repeat(word)
    else:
        print("Error: Invalid function!")


def display_in_a_box(word):
    """Display word in ASCII art box"""
    # Construct box top and side
    box_top = ("###" + ("#" * len(word)) + "###")
    box_side = ("#  " + (" " * len(word)) + "  #")
    # Output box
    print(box_top)
    print(box_side)
    print(f"#  {word}  #")
    print(box_side)
    print(box_top)


def display_lower_case(word):
    """Output lowercase word."""
    print(word.lower())


def display_upper_case(word):
    """Output uppercase word."""
    print(word.upper())


def display_mirrored(word):
    """Output mirrored word."""
    # Initialize variables
    word_mirrored = ""
    # Traverse word backwards, and add char to word_mirrored
    for i in range(len(word) - 1, -1, -1):
        word_mirrored += word[i]
    print(word_mirrored)


def display_repeat(word):
    """Output word repeated x times."""
    repetitions = int(input("How many times should the word repeat?\n"))
    print()
    for _i in range (0, repetitions):
        print(word)


while True:
    print()
    menu()
