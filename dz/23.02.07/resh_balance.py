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
min_l = 0
for number in range(lower_value + 1, 1, -1):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                break
        else:
            if min_l < number:
                min_l = number
                break
max_l = 0
for number in range(upper_value + 1, upper_value * 90):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                break
        else:
            max_l = number
            break

st = False
if len(l) > 1:
    if l[0] == (min_l + l[1]) / 2:
        print(l[0], end=' ')
        st = True

for i in range(1, len(l)):
    if i == len(l)-1:
        if l[i] == (max_l + l[i-1]) / 2:
            print(l[i], end=' ')
            st = True

    else:
        if l[i] == (l[i-1] + l[i+1]) / 2:
            print(l[i], end=' ')
            st = True
if not st:
    print(0)

