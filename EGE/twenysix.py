f = open('26.txt', 'r')

s, n = map(int, f.readline().split())

p = []
for i in range(n):
    p.append(int(f.readline()))
p.sort(reverse=True)

summa = 0
for count in range(0, len(p)):
    if summa + p[count] > s: break
    summa += p[count]
print(count+1)

zapas = s - summa
for i in range(0, len(p)):
    if p[i] - p[count - 1] <= zapas:
        itog = p[i]
print(itog)
