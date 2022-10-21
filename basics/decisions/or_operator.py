"""Demonstrates use of logical or operator."""

type_of_adventure = input("")
if (type_of_adventure == "scary") or (type_of_adventure == "short"):
    print("Entering the dark forest!")
elif (type_of_adventure == "long") or (type_of_adventure == "safe"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")
