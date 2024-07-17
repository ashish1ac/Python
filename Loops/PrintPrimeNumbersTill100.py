print('2')
for i in range(2, 101):
    count = 0
    if i % 2 == 0:  # If any number is even it can't be a prime number, no need to go inside loop
        continue

    for j in range(i):
        if (i % (j+1)) == 0:
            count += 1

    if count == 2:
        print(i, end=' ')
