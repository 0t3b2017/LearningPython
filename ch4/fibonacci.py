# without Memoization - slower 
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

#for n in range(1, 101):
#    print(n, ":", fibonacci(n))

# Memoization - Implement explicity
fibonacci_cache = {}

def fibonacci_c(n):
    # If we have cached the value, the return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_c(n-1) + fibonacci_c(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 50):
    print(n, ":", fibonacci_c(n))


