def check(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


lower_value, upper_value = map(int, input().split())
c = False
l = []
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                break
        else:
            l.append(number)

for i in range(len(l)):
    if check(2 * l[i] + 1):
        print(l[i], end=' ')
        c = True
if not c:
    print(0)
