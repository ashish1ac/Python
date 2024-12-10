romandct = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

num = input("Enter the roman number: ")

if num in romandct:
    print(romandct[num])

i = 0


