"""Call a function passing a parameter
"""


def escape_by(plan):
    """Output a string based on the parameter
    """
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")


escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
