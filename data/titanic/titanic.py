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
        headings.append(next(csv_reader))  # Read CSV headings
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
  [5] Display the number of survivors per age group
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


def display_passengers_per_gender():
    """Display number of passengers per gender from records."""
    males = 0
    females = 0
    for record in records:
        if record[4] == "male":
            males += 1
        else:
            females += 1
    print(f"Females: {females}, males: {males}")
    input("\nPress ENTER to return to menu.")


def display_passengers_per_age_group():
    """Display number of passengers per age group from records."""
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        if record[5] == "":
            pass
        elif float(record[5]) < 18:
            children += 1
        elif float(record[5]) < 65:
            elderly += 1
        else:
            adults += 1
    print(f"Children: {children}, adults: {adults}, elderly: {elderly}")
    input("\nPress ENTER to return to menu.")


def display_survivors_per_age_group():
    """Display number of survivors per age group from records."""
    children_s = 0
    children = 0
    adults_s = 0
    adults = 0
    elderly_s = 0
    elderly = 0
    for record in records:
        if record[5] == "":
            pass
        elif float(record[5]) < 18:
            if record[1] == "1":
                children_s += 1
            children += 1
        elif float(record[5]) < 65:
            if record[1] == "1":
                adults_s += 1
            adults += 1
        else:
            if record[1] == "1":
                elderly_s += 1
            elderly += 1
        print(children)
    print(f"Children: {children_s}/{children}, adults: {adults_s}/{adults}" +
          f", elderly: {elderly_s}/{elderly}")
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
        elif choice == 3:
            display_passengers_per_gender()
        elif choice == 4:
            display_passengers_per_age_group()
        elif choice == 5:
            display_survivors_per_age_group()
        else:
            print("Error: No corresponding function.\n")


if __name__ == "__main__":
    run()
