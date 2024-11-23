"""
We need to take input from the user the number of working hours in a list.
Need to add all the hours and multiply by the hourly wages
"""
hourList = []
for i in range(5):
    hourList.append(input("Enter the number of hours day by day!: "))

# Above task can we achieved in a simle way as well
'''
work_hours = input('Enter the number of hours, separated by comma: ).split()
It will populate the work_hours with the hours as string type
'''

sum = 0
for j in range(len(hourList)):
    sum = sum + int(hourList[j])  # Why I need to convert this into int because input returns the String

print(sum * 10)

