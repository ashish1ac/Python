"""
If we divide a number by 2, either we get 0 or 1. This is basically represent the binary form.
Logic is, get the modulus of the number by 2 -> 1 or 0 is the binary
floor divide the number (//) by 2 to reduce the number.

Here, interesting thing is we will get the reverse of the actual binary number.
To get, the real we have to reverse the number.
"""

number = int(input("Enter the number: "))
binary = 0
act_binary = 0

while number > 0:
    r = number % 2
    number = number // 2
    binary = binary * 10 + r

print(binary)

while binary > 0:
    r = binary % 10
    act_binary = act_binary * 10 + r
    binary = binary // 10

print(act_binary)