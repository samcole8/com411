"""
Simple program to convert an ASCII character to it's corresponding ASCII code
"""

print("Program Started!")
character = input("Please enter a standard ASCII character:\n")
if len(character) == 1:
    print(ord(character)) # Converts character to ASCII code
else:
    print("Error: More than one character entered.")
print("Program Ended!")
