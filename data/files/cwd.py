"""Outputs the current working directory and it's contents."""

import os


def cwd():
    """Get cwd and output directory contents."""
    path = os.getcwd()
    print(f"The current working directory is '{path}'")
    print("The directory contains the following files: ")
    for file in os.listdir(path):
        print(f"{file} ", end="")


def run():
    """Run the program."""
    cwd()


if __name__ == "__main__":
    run()
