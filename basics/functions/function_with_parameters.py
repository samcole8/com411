""" Simple script demonstrating a function with two parameters.
"""

def climb_ladder(steps_remaining, steps_crossed):
    """ Code using two parameters
    """
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")

climb_ladder(5, 2)
climb_ladder(2, 5)
