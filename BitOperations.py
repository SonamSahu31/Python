# Initialize val
val = 0xCAFE
# Task 1: Test if at least three of the last four bits (LSB) are on
last_four = val & 0xF
count = ((last_four & 1) + 
         ((last_four >> 1) & 1) + 
         ((last_four >> 2) & 1) + 
         ((last_four >> 3) & 1))
at_least_three = count >= 3
print(f"At least three LSB on: {'Yes' if at_least_three else 'No'}")
# Task 2: Reverse the byte order (produce val=0xFECA)
reversed_val = ((val & 0xFF) << 8) | ((val >> 8) & 0xFF)
print(f"Reversed byte order: 0x{reversed_val:04X}")
# Task 3: Rotate four bits (produce val=0xECAF)
rotated = ((val >> 4) | (val << 12)) & 0xFFFF
print(f"Rotated four bits: 0x{rotated:04X}")
