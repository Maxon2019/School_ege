n, q = map(int, input().split())
n_l = list(map(int, input().split()))
q_l = list(map(int, input().split()))
n_l = sorted(n_l)

for i in q_l:
    c = 0
    while i > 0 and c < n:
        i -= n_l[c]
        c += 1
    if i < 0:
        print(c - 1, end=' ')
    else:
        print(c, end=' ')
