n, m = map(int, input().split())

all_s = ''

for i in range(n):
    all_s += input()

k = int(input())
spi = []
for i in range(k):
    cur_s = input()
    n = all_s.count(cur_s)
    if n > 0:
        spi.append([cur_s, n])
spi = sorted(spi)

for i in spi:
    print(*i)
