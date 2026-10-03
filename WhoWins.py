# Input total number of stones
N = int(input())

i = 1  # round counter
remaining = N

while True:
    # Ramesh's turn
    remaining -= i
    if remaining <= 0:
        print("Ramesh")
        break

    # Suresh's turn
    remaining -= i * 2
    if remaining <= 0:
        print("Suresh")
        break

    # Move to next round
    i += 1
