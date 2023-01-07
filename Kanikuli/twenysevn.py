f = open('27-B.txt')
n = int(f.readline())
# a = [int(x) for x in f]

"""
# A
count = 0
for i in range(n):
    for j in range(i+1,n):
        if (a[i] + a[j])% 4 == 0 and a[i]*a[j] % 6561==0:
            count+=1
print(count)"""

ost = [[0] * 9 for i in range(4)]
count_nums = 0
for i in range(n):
    x = int(f.readline())
    c3 = 0
    o4 = x % 4
    while x % 3 == 0:
        x //= 3
        c3 += 1
    if c3 >= 8:
        c3 = 8
    ost[o4][c3] += 1

    obr_ost = (4 - o4) % 4
    for j in range(8 - c3, 9):
        count_nums += ost[obr_ost][j]
print(count_nums)