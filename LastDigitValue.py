N = int(input())  # number of test cases

for _ in range(N):
    a, b = map(int, input().split())

    # Since 0^0 is undefined, but problem says a and b are not both 0
    if b == 0:
        print(1)
        continue

    # Last digit cycles repeat every 4 for most numbers
    cycle = [a % 10]
    next_digit = (cycle[-1] * a) % 10

    # Build cycle of last digits until it repeats
    while next_digit not in cycle:
        cycle.append(next_digit)
        next_digit = (next_digit * a) % 10

    # Determine position in cycle (b-1 because of 0-indexing)
    last_digit = cycle[(b - 1) % len(cycle)]

    print(last_digit)
