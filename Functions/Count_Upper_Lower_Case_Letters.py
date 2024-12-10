"""
You are given a string containing the Upper and Lower case letters, you need to find the count of Uppercase and
lowercase letters.
"""


def countUpperLowerCase(str):
    newStr = str
    uCount = 0
    lCount = 0

    for i in newStr:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uCount += 1
        elif i in "abcdefghijklmnopqrstuvwxyz":
            lCount += 1

    return f"Upper Count: {uCount} Lower Count: {lCount}"


msg = "abcdgbbdeibruydbddbdrtyusgABCDEFGHUIJHJ"
print(countUpperLowerCase(msg))






