k, n = map(int, input().split())

a = [i for i in range(n + 1)]
a[1] = 0
i = 2
while i <= n:
    if a[i] != 0:

        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1

a = set(a)

a.remove(0)
a = list(a)
a.sort()
a = a[::-1]
for i in range(0, len(a)):
    if a[i] <= k:
        a = a[::-1]
        a = a[i + 1:]
        break
if max(a) < k:
    print(0)
else:
    print(*a)
