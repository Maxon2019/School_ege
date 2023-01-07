m = []
for i in range(100,1000):
    m.append(str(i))

s = int(''.join(m))
print(s % 7)