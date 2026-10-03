T = int(input())  # number of test cases

for _ in range(T):
    N = int(input())  # number of lemon cakes

    # Best package size A that maximizes leftover cakes
    best_A = (N // 2) + 1

    # Output the result
    print(best_A)
