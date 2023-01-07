import math


def f(x):
    return x ** 2 - 14 * math.floor(3 * x) + 152

m = []

for j in range(-10000000,100000001):
    if f(j) == 0:
        m.append(j)
print(m)
print(m[0]**2+m[1]**2)
