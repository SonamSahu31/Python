# Ramesh's Partner Selection Problem

# Input number of people
N = int(input())

# Input minimum skill required
X = int(input())

# Loop through each person's skill and check
for _ in range(N):
    Y = int(input())
    if Y >= X:
        print("YES")
    else:
        print("NO")
