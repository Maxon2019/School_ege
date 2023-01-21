"""for x in range(10000):
    ans = not (x ** 2 - 7 > 15) or (x ** 2 + 8 < 35)
    if ans:
        print(x)
"""
s = 0
for i in range(100, 1000):
    if i % 5 == 1:
        s += i
print(s)
