n = int(input("Enter the number: "))
reverse_number = ''

while n > 0:
    digit = n % 10
    # print(digit)  # This gives reverse number in next line ...
    reverse_number = reverse_number * 10 + digit
    n = n // 10

print("The reverse number is:", reverse_number)
