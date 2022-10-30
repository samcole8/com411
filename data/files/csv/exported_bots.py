"""Write data to CSV file."""


def export(path, number_of_bots):
    """Write data to CSV file."""
    print("\nExporting...")
    with open(path, "a", encoding="utf-8") as file:
        for _i in range(0, number_of_bots):
            bot_id = input("\nEnter the bot ID:")
            bot_name = input("\nEnter the bot name:")
            bot_paint = input("\nEnter the bot paint:")
            file.write(f"\n{bot_id},{bot_name},{bot_paint}")


def run():
    """Run the program."""
    path = "/home/sam/mygit/com411/data/files/csv/exported_bots.csv"
    number_of_bots = int(input("Enter number of bots to export:"))
    export(path, number_of_bots)


if __name__ == "__main__":
    run()
