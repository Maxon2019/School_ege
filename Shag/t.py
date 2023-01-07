def mas(q, a=[], b=[], c=[]):
    if len(q) == 0:
        return min(len(a), len(b), len(c)) * (sum(a) == sum(b) == sum(c))
    s, t = q[1:], [q[0]]
    return mas(s, a + t, b, c) or mas(s, a, b + t, c) or mas(s, a, b, c + t)


k = input()  # ne nado
m = [int(v) for v in input().split()]
print(0 if sum(m) % 3 or 3 * max(m) > sum(m) else mas(sorted(m)))
