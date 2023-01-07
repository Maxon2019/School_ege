n = int(input())
s = int(input())

c = 0
r = 0

for i in range(n):
    cur_v = int(input())
    if cur_v + r <= s:
        r += cur_v
    else:
        c += cur_v

print(r, c, sep='\n')
