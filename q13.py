def is_perfect_square(x):
    return int(x**0.5)**2 == x

def is_fibonacci(n):
    return is_perfect_square(5 * n**2 + 4) or is_perfect_square(5 * n**2 - 4)

# Ask for a number N from the user
N = int(input("Enter a number to check if it's a member of the Fibonacci series: "))

# Check if N is a member of the Fibonacci series
if is_fibonacci(N):
    print(N, "is a member of the Fibonacci series.")
else:
    print(N, "is not a member of the Fibonacci series.")
