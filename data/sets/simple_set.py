"""Demonstrate use of a simple set."""


def observed():
    """Create and return set."""
    observation = set({
                       "Flying Car", 
                       "Sky Scraper",
                       "Sky Scraper",
                       "Laser",
                       "Dome",
                       "Dome"
                       })
    return observation


def run():
    """Run the program."""
    print(observed())


if __name__ == "__main__":
    run()
