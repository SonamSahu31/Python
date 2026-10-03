from math import factorial

# Function to calculate nCr
def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Input number of rows
N = int(input("Enter number of rows: "))

# Generate Pascal's Triangle
for i in range(N):
    row = []
    for j in range(i + 1):
        row.append(str(nCr(i, j)))
    print(" ".join(row))
