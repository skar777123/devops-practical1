def sum_of_digits(n):
    # abs(n) handles negative numbers properly
    return sum(int(digit) for digit in str(abs(n)))

# Example:
print(sum_of_digits(12345))  # Output: 15 (1+2+3+4+5)

def sum_of_digits_math(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10  # Get the last digit
        n //= 10         # Remove the last digit
    return total

# Example:
print(sum_of_digits_math(12345))  # Output: 15

def reverse_number(n):
    # Handle negative signs
    sign = -1 if n < 0 else 1
    # Convert to string, reverse using [::-1], convert back to int
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num

# Example:
print(reverse_number(12345))  # Output: 54321