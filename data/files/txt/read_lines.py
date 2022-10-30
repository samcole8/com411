"""Reads a text file line by line."""


def search(path):
    """Open text file and print each line with appended text."""
    print("Searching...")
    with open(path, encoding="utf-8") as file:
        line_list = file.readlines()
        for line in line_list:
            line = line.strip('\n')  # Strip newline character.
            print(f"Looked in location {line}.")
    print("...Done!")


def run():
    """Run the program."""
    path = "/home/sam/mygit/com411/data/files/txt/library.txt"
    search(path)


if __name__ == "__main__":
    run()
