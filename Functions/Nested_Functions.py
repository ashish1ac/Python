def outer(msg, name):

    def inner():
        print('*' * 27)
        print(msg, name)
        print('*' * 27)

    return inner()


d = outer
d("Welcome to the team!", "Ashish")


