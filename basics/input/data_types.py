# Take inputs for display later
name = input("What is your name human?\n")
age = input("\nHow old are you (in years)?\n")

# Take inputs for calculation later
height = float(input("\nHow tall are you (in metres)?\n"))
weight = float(input("\nHow much do you weigh (in kilograms)?\n"))

# Calculate BMI based on previous inputs
BMI = (weight 
    / (height ** 2))

# Output string
print(f"{name} you are {age} years old and your BMI is {BMI}.")