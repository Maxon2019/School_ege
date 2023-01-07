f = open('17.txt', 'r')

f = f.readlines()
mi = 10000000
for i in range(len(f)):
    f[i] = int(f[i])
    if f[i] < mi and f[i] % 10 == 5:
        mi = f[i]
m = mi ** 2
ma = 0
c = 0
for i in range(len(f) - 1):
    if f[i] <= f[i + 1]:
        if f[i] % 10 == 5:
            if f[i] ** 2 + f[i + 1] ** 2 < m:
                c += 1
                if f[i] ** 2 + f[i + 1] ** 2 > ma:
                    ma = f[i] ** 2 + f[i + 1] ** 2


    else:
        if f[i + 1] % 10 == 5:
            if f[i] ** 2 + f[i + 1] ** 2 < m:
                c += 1
                if f[i] ** 2 + f[i + 1] ** 2 > ma:
                    ma = f[i] ** 2 + f[i + 1] ** 2

print(c,ma)