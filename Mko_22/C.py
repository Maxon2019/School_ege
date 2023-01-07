def primfacs(um):
    i = 2
    primfac = []
    while i * i <= um:
        while um % i == 0:
            primfac.append(i)
            um = um / i
        i = i + 1
    if um > 1:
        primfac.append(int(um))
    return primfac


def delenie(num, c):
    r = 0
    while num > 0:
        num //= c
        r += num
    return r


n, p = map(int, input().split())

l = primfacs(p)

list_d = []

for i in l:
    col = l.count(i)
    if col > 1:
        list_d.append(int(delenie(n, i) / col))
    else:
        list_d.append(delenie(n, i))
print(min(list_d))
