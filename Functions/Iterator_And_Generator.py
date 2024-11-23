"This is about iterator"
lst = [1, 2, 3, 4, 5]
itr = iter(lst)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

print("------------------")

'This is all about generator'


def days():
    lstOfDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    i = 0
    while True:
        x = lstOfDays[i]
        i = (i + 1) % 7
        yield x


itr = days()
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

print("LOCALS:", locals())
print("GLOBALS", globals())
