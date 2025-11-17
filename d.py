# Read 4 space-separated integers
A, B, C, D = map(int, input().split())
 
# Calculate the difference
difference = (A * B) - (C * D)
 
# Print the result in the required format
print(f"Difference = {difference}")