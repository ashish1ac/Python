"""
If amount <= 1000 -> discount offered will be: 10%
If 1000 <= amount <= 5000 -> discount offered will be: 20%
If 5000 <= amount <= 10000 -> discount offered will be: 30%
If amount >= 10,000 -> discount offered will be: 50%

Based on this we have to calculate the discount amount
"""

amount = int(input("Enter the total amount: "))

if amount <= 1000:
    discount = amount * 0.10
elif 1000 < amount <= 5000:
    discount = amount * 0.20
elif 5000 < amount <= 10000:
    discount = amount * 0.30
else:
    discount = amount * 0.50

print("Discount get:", discount)
print("You need to pay:", (amount - discount))
