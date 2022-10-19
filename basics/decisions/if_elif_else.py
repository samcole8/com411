"""
Simple if/elif/else statement
"""

direction = input("In which direction should I paint?\n")
if direction == "up":
    print("I am painting in the upward direction!")
elif direction == "down":
    print("I am painting in the downward direction!")
elif direction == "left":
    print("I am painting in the left direction!")
else:
    print("I am painting in the right direction!")
