

# Take inputs for each variable
number_of_lives = int(input("Please enter the number of lives.\n"))
energy_level = int(input("\nPlease enter the energy level.\n"))
shield_level = int(input("\nPlease enter the shielf level\n"))

# Convert numeric inputs to concatenated strings
lives_string = "♥" * number_of_lives
energy_string = "♦" * energy_level
shield_string = "♦" * shield_level

# Print strings
print(f"Lives: {lives_string}")
print(f"Energy: {energy_string}")
print(f"Shield: {shield_string}")

