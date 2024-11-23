def fun(a, b, c):
    print(a, b, c)


lst = [1, 2, 3]
st = {10, 20, 30}
tpl = (11, 22, 33)

"""
"This is the traditional way to do that, we've 3 args and a list of 3 elements

print(fun(lst[0], lst[1], lst[2]))
"""

"""
can't we pass the list directly with 3 elements, it will throw error by saying I got only 1 param instead of 3.
print(lst)
"""

"So the correct way to pass the list is *lst, but make sure number of args required by the fun should be the same as the number of elements in the lst"
print(fun(*lst))
print(fun(*st))
print(fun(*tpl))