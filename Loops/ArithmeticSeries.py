"""
We need to print the n terms of the AP,
User will give the a, d of the AP.
"""

a = int(input("Enter the first term of the AP: "))
d = int(input("Enter the common difference of the AP: "))
n = int(input("How many terms you want: "))

print(a)
for i in range(1, n):
    a = a + d
    print(a)

