""" Demonstrates the use of a function with a loop
"""

def cross_bridge(distance_crossed):
    """ Simple for loop inside of a functiion
    """
    for i in range(0, distance_crossed):
        print("Crossed step.")
    if distance_crossed > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

cross_bridge(3)
cross_bridge(6)
