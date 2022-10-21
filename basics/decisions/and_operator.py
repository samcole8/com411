"""Demonstrates use of logical and operator."""

heard = input("What did I hear?\n")
seen = input("\nWhat did I see?\n")

if (heard == "grrr") and (seen == "big red eyes"):
    print("\nThere is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")
