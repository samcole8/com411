"""Write to a json file."""


import json


def read(path):
    """Read from json file."""
    print("Reading...")
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    print("...Done!")
    return data


def save(path, data):
    """Write to json file."""
    print("Exporting...")
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def run():
    """Run the program."""
    path = "/home/sam/mygit/com411/data/files/json/exported.json"
    data = read("/home/sam/mygit/com411/data/files/json/robocity.json")
    save(path, data)


if __name__ == "__main__":
    run()
