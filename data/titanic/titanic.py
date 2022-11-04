"""Looking at the Titanic data."""


import csv


records = []
headings = []


def load_data(file_path):
    """Load data from CSV file into headings."""
    print("Loading data...")
    # Open CSV file
    with open(file_path, encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        headings.append(csv_reader)  # Read CSV headings into global variable
        # Read remaining records
        for record in csv_reader:
            records.append(record)
    print(f"Done! Successfully loaded {len(records)} records.")


def run():
    """Run the program."""
    load_data("/home/sam/mygit/com411/data/titanic/titanic.csv")


if __name__ == "__main__":
    run()
