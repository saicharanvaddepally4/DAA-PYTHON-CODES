
def factorial(n):
    if n == 0 or n == 1:  # Base condition
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

num = 5
print(factorial(num))
