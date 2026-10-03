import math

# Input number of test cases
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    
    # Calculate GCD
    gcd = math.gcd(X, Y)
    
    # Calculate LCM
    lcm = (X * Y) // gcd
    
    # Output LCM and GCD
    print(lcm, gcd)
