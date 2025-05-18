


def func1 (a):
    a += 1
    return a

def func2( a):
    a *= a
    return a

def func3(b):
    b = func2(b)
    b -= b
    return b

a = 5

c = func1(a)
print(c)
print(a)
a = func2(a)
d = func3(a)