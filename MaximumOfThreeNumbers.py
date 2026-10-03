def find_max(a, b, c):
    # Using ternary operator to find the maximum
    return a if a > b and a > c else (b if b > c else c)
# Example usage
num1 = 10
num2 = 25
num3 = 15
maximum = find_max(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is {maximum}")