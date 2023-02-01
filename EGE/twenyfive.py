targ = 460000

for num in range(135790, 163229):
    c = 0
    s = 0
    i = 2
    while i ** 2 < num:
        if num % i == 0:
            c += 2
            s += i + num // i
        i += 1

    if i ** 2 == num:
        c += 1
        s += i

    if s > targ:
        print(c, s)
"""
142 473759
118 462767
126 464999
118 461969
118 477071
"""