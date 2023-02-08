def check(li):

    c = True
    for i in range(0, len(li) - 1):
        if li[i] <= li[i + 1]:
            c = False
    return c


lower_value, upper_value = map(int, input().split())
c = False
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                break
        else:
            l = list(map(int, list(str(number))))
            ll = sorted(l)[::-1]
            k = check(ll)
            if l == ll and k:
                c = True
                print(number, end=' ')
if not c:
    print(0)
