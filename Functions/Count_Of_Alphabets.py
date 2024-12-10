"""
str = "aaaaabbbbcccdde"
o/p = a5b4c3d2e1
"""


def countingAlphabets(input_string):
    element_count = {}
    result_string = ""

    for char in input_string:
        if char in element_count:
            element_count[char] += 1
        else:
            element_count[char] = 1

    for item in element_count:
        print(str(item) + str(element_count[item]), end='')

    return result_string


countingAlphabets("aaaaabbbbcccddeAAAA")
