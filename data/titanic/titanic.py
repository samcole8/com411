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


def display_menu():
    """Display function menu."""
    choice = int(input("""
Please select one of the following options:

  [1] Display the names of all passengers
  [2] Display the number of passengers that survived
  [3] Display the number of passengers per gender
  [4] Display the number of passengers per age group
  \n: """))
    return choice


def display_passenger_names():
    """Display passenger names from records."""
    print("The names of the passengers are:")
    for record in records:
        print(record[3])
    input("\nPress ENTER to return to menu.")


def display_num_survivors():
    """Display number of survivors from records."""
    count = 0
    for record in records:
        if record[1] == "1":
            count = count + 1
    print(f"{count} passengers survived.")
    input("\nPress ENTER to return to menu.")


def run():
    """Run the program."""
    load_data("/home/sam/mygit/com411/data/titanic/titanic.csv")
    # Menu choice
    while True:
        choice = display_menu()
        if choice == 1:
            display_passenger_names()
        elif choice == 2:
            display_num_survivors()
        else:
            print("Error: No corresponding function.\n")


if __name__ == "__main__":
    run()
