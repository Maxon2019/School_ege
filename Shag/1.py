n = list(input())

m = -1
ind = 0
for i in range(0,len(n)):
    n[i] = int(n[i])
    if n[i] > m:
        m = n[i]
        ind = i
    n[i] = str(n[i])

n_f = int(''.join(n))
n[ind] = str(m+3)
print(int(''.join(n)) - n_f)

