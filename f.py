# Read two integers from input
N, M = map(int, input().split())
 
# Find the last digits
last_digit_N = N % 10
last_digit_M = M % 10
 
# Sum the last digits
result = last_digit_N + last_digit_M
 
# Print the result
print(result)