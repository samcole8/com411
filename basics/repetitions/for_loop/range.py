"""
Example script showing for loop counting in twos
"""

req_brightness = int(input("What level of brightness is required?\n"))
print("Adjusting brightness...\n")
for current_brightness in range(0, req_brightness, 2):
    print("Beep's brightness level: **" + "*" * current_brightness)
    print("Bop's brightness level: **" + "*" * current_brightness)
print("\nAdjustments complete!")
