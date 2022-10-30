"""Read from CSV."""


import csv


def read(path):
    """Read from CSV."""
    with open(path, encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print("Values:")
        for values in csv_reader:
            print(values)


def run():
    """Run the program."""
    path = "/home/sam/mygit/com411/data/files/csv/bots.csv"
    read(path)


if __name__ == "__main__":
    run()
