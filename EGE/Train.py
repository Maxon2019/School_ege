'''for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((y == w) or (not(z) or w)) and (y == (x or z)) == 1:
                    print(z, y, x, w)'''
s = '1' * 77

while s.find('111') != -1:
    s = s.replace('111', '2',1)
    s = s.replace('222', '11',1)

print(s)

'''n = int(input.txt())
k = 0
s = 0
while n > 0: # 4
    d = n % 10
    if d % 3 == 0:
        k += 1
        s += d
    n = n // 10
if k > 0:
    print(k, s)
else:
    print("NO")
#3 18
#300
'''

"""# m,k
a = []
k = 0
m = []
N = 5
for i in range(0, N):
    a.append(int(input.txt()))
    if a[i] % 3 != 0 and a[i] % 2 == 0:
        k += 1
    elif a[i] % 3 == 0 and a[i] % 2 == 1:
        m.append(i)
for i in range(len(m)):
  a[m[i]] = k

print(*a)"""

"""f = 8
for s in range(1,27):
    if """
