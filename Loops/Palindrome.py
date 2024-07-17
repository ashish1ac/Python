"""
Check whether the number is Palindrome or not.
"""

number = int(input("Enter the number: "))
actual_number = number
reverse_number = 0

while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number = number // 10

if actual_number == reverse_number:
    print("Number is Palindrome!")
else:
    print("Number is not Palindrome!")

