# Check whether the person is eligible for work: Person age must be in between 18 and 60.

age = int(input("Enter the age of the person: "))

if 18 <= age <= 60:
    print("You're eligible for the work!")
else:
    print("You're not eligible for the work!")

