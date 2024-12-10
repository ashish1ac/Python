student = {}

for i in range(2):
    name = input("Enter the name of the student: ")
    rNo = input("Enter the roll number of the number: ")
    dept_name = input("Enter the department name of the student: ")

    if name not in student:
        student[name] = {"name": name, "Roll No": rNo, "Dept_Name": dept_name}
    else:
        print("Name is already there in the dictionary!")

print(student)
