i = 10
f = 15.20
b = True
c = 10 + 3j
s1 = "Ashish"
s2 = '123'
s3 = '0b1111'

print(int(f))
print(int(b))
# we cant convert complex number into int
'print(int(c))'

# we cant convert string containing letters into int
'print(int(s1))'

# String containing numbers can be converted to int
print(int(s2))
print(int(s3, 2))

# To generate a complex number use complex fun
cn = complex(10, 20)
print(cn)
