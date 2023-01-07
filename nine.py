f = open('nine_t.txt', 'r')

f = f.readlines()
for i in range(len(f)):
    f[i] = f[i][::-1][1::][::-1].split()
    for j in range(5):
        f[i][j] = int(f[i][j])
    f[i] = sorted(f[i])

print(f)
c = 0
for k in range(len(f)):
    flag = True
    nec = []
    ch = []
    for n in range(4):
        if f[k][n] == f[k][n + 1]:
            flag = False
            break
    if flag:  # True
        for n in range(5):
            if f[k][n] % 2 == 0:
                ch.append(f[k][n])
            else:
                nec.append(f[k][n])
        if len(nec) > len(ch) and sum(nec) < sum(ch):
            c += 1
print(c)
