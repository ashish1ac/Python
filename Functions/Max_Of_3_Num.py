def maxOfThree(a, b, c):
    if a > b and a > c:
        print(f"{a} is the highest among {a, b, c}")
    elif b > a and b > c:
        print(f"{b} is the highest among {a, b, c}")
    else:
        print(f"{c} is the highest among {a, b, c}")


def optimizedSolution(a, b, c):
    highest = a  # Assume 'a' is the highest initially
    if b > highest:
        highest = b
    if c > highest:
        highest = c

    print(f"{highest} is the highest among {a, b, c}")


print(optimizedSolution(20, 45, 10))
print(maxOfThree(20, 15, 10))
print(optimizedSolution(-19, -10, -30))
