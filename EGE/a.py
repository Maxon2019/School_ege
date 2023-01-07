n = int(input())
c = list(map(int, input().split()))
d = list(map(int, input().split()))
a = []
for i in range(n):
    o = c[i] + d[i]

    a.append(int(o/2))
print(*a)