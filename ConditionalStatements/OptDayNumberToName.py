# Optimize version of DayNumber to Name code using dictionary

day_number = int(input("Enter the number of the day: "))

days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

if 1 <= day_number <= 7:
    print(f"It's {days[day_number]}!!")
else:
    print("Please enter a day number between 1 to 7, Thank you!!")
