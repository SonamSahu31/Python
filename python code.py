import math
# Given values
radius = 42
angle_degrees = 60
# Convert angle to radians
angle_radians = math.radians(angle_degrees)
# Calculate arc length
arc_length = radius * angle_radians
# Perimeter of square is the arc length
perimeter = arc_length
# Side length of square
side_length = perimeter / 4
# Area of square
area = side_length ** 2
# Print the result
print(f"The area of the square is {area:.2f} square units.")