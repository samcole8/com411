"""Performs multiple read operations on a text file."""


def display_chars(path, number_of_chars):
    """Open file and output specified number of characters."""
    with open(path, encoding="utf-8") as file:
        print(file.read(number_of_chars))


def display_line(path):
    """Open file and output first line."""
    with open(path, encoding="utf-8") as file:
        print(file.readline())


def display_text(path):
    """Open file and output contents."""
    with open(path, encoding="utf-8") as file:
        print(file.read())


def run():
    """Run the program."""
    path = "/home/sam/mygit/com411/data/files/txt/library.txt"
    display_chars(path, 5)
    display_line(path)
    display_text(path)


if __name__ == "__main__":
    run()
