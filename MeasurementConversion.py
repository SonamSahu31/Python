# Program to convert inches to feet, yards, centimeters, and meters
# Conversion factors
INCH_TO_FOOT = 1 / 12
INCH_TO_YARD = 1 / 36
INCH_TO_CM = 2.54
INCH_TO_METER = 1 / 39.37
# Get user input
inches = float(input("Enter the measurement in inches: "))
# Perform conversions
feet = inches * INCH_TO_FOOT
yards = inches * INCH_TO_YARD
centimeters = inches * INCH_TO_CM
meters = inches * INCH_TO_METER
# Print results
print(f"\nConversions for {inches} inches:")
print(f"1. Feet: {feet:.2f} ft")
print(f"2. Yards: {yards:.2f} yd")
print(f"3. Centimeters: {centimeters:.2f} cm")
print(f"4. Meters: {meters:.2f} m")
