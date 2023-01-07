import math

print(math.floor(1.7))
print(math.floor(-1.7))
m = []
for i in range(0,100):
    an = math.floor(6*i)+math.floor(18*i)+math.floor(22*i)+math.floor(33*i)+math.floor(3.5*i)
    if an not in m:
        m.append(an)

print(m)
print(len(m))