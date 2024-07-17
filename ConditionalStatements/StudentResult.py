# Check If a student failed or passed, by taking marks in 3 subjects.

marksInPhysics = int(input("Enter your marks in Physics: "))
marksInChemistry = int(input("Enter your marks in Chemistry: "))
marksInMaths = int(input("Enter your marks in Maths: "))

if marksInPhysics >= 33 and marksInChemistry >= 33 and marksInMaths >= 33:
    print("Student has Passed!")
else:
    print("Student has Failed!")
