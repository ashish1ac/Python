# Quadratic Equation Means : ax2 + bx + c = 0

a = int(input("Enter the a of the Quadratic Equation "))
b = int(input("Enter the b of the Quadratic Equation "))
c = int(input("Enter the c of the Quadratic Equation "))

root1 = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
root2 = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)

print("These are the roots of the quadratic equations", root1, root2)
