"""Extract values from a CSV file by index."""

import csv


def extract(path):
    """Extract values from a CSV file by index."""
    print("Extracting...")
    with open(path, encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names = ""
        for value in csv_reader:
            names += f"{value[1]}\n"
    print("Done! The extracted names are as follows:")
    print(names)


def run():
    """Run the program."""
    path = "/home/sam/mygit/com411/data/files/csv/bots.csv"
    extract(path)


if __name__ == "__main__":
    run()
