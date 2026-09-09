# Factorial

def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1