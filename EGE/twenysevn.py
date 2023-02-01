f = open("27-A.txt")  # для файла A замените название
s = f.readlines()
n = int(s[0])  # количество пар
su = 0
d = 10 ** 6
msu = 0
for i in range(1, n + 1):
    x, y = map(int, s[i].split())
    msu += min(x, y)

for i in range(1, n + 1):
    x, y = map(int, s[i].split())
    su += max(x, y)
    if abs(x - y) % 7 == msu % 7:
        d = min(d, abs(x - y))
if su % 7 == msu % 7:
    print(su)
else:
    print(su - d)
