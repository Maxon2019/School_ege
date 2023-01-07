import random

min = 200000

for i in range(1,100000):
    for j in range(1,10000):
        n = i/j+225*j/(i+j)
        if n < min:
            min = n
            ab = i/j
print(min,ab)

