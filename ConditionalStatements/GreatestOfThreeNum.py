a = int(input("Enter the Number A: "))
b = int(input("Enter the Number B: "))
c = int(input("Enter the Number C: "))

if a >= b and a >= c:
    print("A is the greatest!")
elif b >= a and b >= c:
    print("B is the greatest!")
else:
    print("C is the greatest!")

