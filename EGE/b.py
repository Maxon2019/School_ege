a1 = int(input())
r1 = (a1 % 2 == 0)
max1 = a1
max2 = 0
while a1 != 0:
    a1 = int(input())
    if a1 % 2 == 0 and a1 != 0:
        r1 = 1
        if max2 < a1:
            max2 = a1
            max1 = max2
        elif max1 < a1:
            max1 = a1


if r1:
    print('YES')
    print(max1,max2)
else:
    print('NO')