# Function to find nth term and sum of AP
def ap_calculations(a, d, n):
    # nth term
    nth_term = a + (n - 1) * d
    
    # Sum up to nth term
    sum_n = n / 2 * (2 * a + (n - 1) * d)
    
    return nth_term, sum_n
# Example usage
a = 2  # First term
d = 3  # Common difference
n = 5  # nth term
nth_term, sum_n = ap_calculations(a, d, n)
print(f"The {n}th term is: {nth_term}")
print(f"The sum up to {n}th term is: {sum_n}")
