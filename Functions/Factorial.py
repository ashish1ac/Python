def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print("FACTORIAL", factorial(5))


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
        return res


print("FIBONACCI", fibonacci(5))