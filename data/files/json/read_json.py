"""Read from json file."""


import json


def read(path):
    """Read from json file."""
    with open(path, encoding="utf-8") as file:
        data = json.load(file)

        # Print city data
        print(f"City name: {data['city']}")
        print(f"Population size: {data['population']}\n")

        # For each bot in data
        for bot in data["bots"]:
            # Determine name
            name = bot["name"]

            # Determine speed and strength
            stats = bot["stats"]
            speed = stats["speed"]
            strength = stats["strength"]

            # Output to user
            print(f"{name} has a strength level of {speed} ", end="")
            print(f"and a speed level of {strength}.")


def run():
    """Run the program."""
    path = "/home/sam/mygit/com411/data/files/json/robocity.json"
    read(path)


if __name__ == "__main__":
    run()
