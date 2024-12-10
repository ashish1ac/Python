"""
0 <= age <= 13 -> kid
13 < age <= 19 -> teen
19 < age <= 50 -> young
age > 50 -> Older
"""


def stage(age):
    if 0 <= age <= 13:
        print("He is a Kid")
    if 13 < age <= 19:
        print("He is a Teen")
    if 19 < age <= 50:
        print("He is a Young")
    if age > 50:
        print("He is Older")
    try:
        if age < 0:
            print("Negative Value Exception")
    except:
        raise Exception


stage(-10)
