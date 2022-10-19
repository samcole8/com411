"""
Example script using a for loop to break down a string into characters
"""

characters = input("What strange characters do you see?\n")
print("Identifying...\n")
for index in range(0, len(characters)):
    print(f"Index {index}: {characters[index]}") # pylint: disable-msg
print("\nDone!")
