"""Demonstrates counting with a simple while loop."""

number_of_cables = int(input("How many live cables should I avoid?\n"))
print()
count = 0  # pylint: disable-msg=C0103
while count < number_of_cables:
    count += 1
    print(f"Avoiding...Done! {count} live cables avoided.")
print("All live cables have been avoided.")
