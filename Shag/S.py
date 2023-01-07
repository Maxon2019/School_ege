def tri(n, res=[]):
    while n > 0:
        res.append(str(n % 3))
        n = n // 3

    return ''.join(res[::-1])


num = list(reversed(list(map(int, str(tri(int(input())))))))
print(num)
state = 1
for i in range(len(num)-2):
    if num[i] == 0 and num[i + 1] == 1 and num[i + 2] == 2:
        print(i + 1)
        state = 0
        break

if state:
    print(0)
