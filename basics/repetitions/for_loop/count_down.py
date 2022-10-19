"""
Example script to count down using a for loop
"""

step_number = int(input("How many steps until we reach the cave?\n"))
print()
for remaining_steps in range(step_number, 0, -1):
    print(f"{remaining_steps} steps remaining")
print("\nWe have reached the cave!\n")
