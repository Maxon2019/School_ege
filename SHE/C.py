n, k, m, alla = map(int, input().split())

len_we = k * (n - 1) + m

a = alla % len_we
c = 0
while a > -1:
    if c == n:
        print(n, '\n')
        break
    else:
        a -= k
    c += 1

print(c)
