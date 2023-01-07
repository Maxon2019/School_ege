for a in range(1, 1000):
    st = 0
    for x in range(1, 1001):
        for y in range(1, 1001):
            st += int(not (144 % x == 0) or not (x % y == 0) or (x + y > 100) or (a - x > y))
    print(st,a)
