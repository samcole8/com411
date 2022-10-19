"""
Simple program to convert an ASCII code to it's corresponding ASCII character
"""

print("Program Started!")
code = int(input("Please enter an ASCII character:\n"))
if code in range(32, 127): # Between 32 and 126
    print(chr(code)) # Converts ASCII code to a character
else:
    print("Error: Code out of range.")
print("Program Ended!")
