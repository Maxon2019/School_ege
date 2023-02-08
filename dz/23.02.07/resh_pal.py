lower_value, upper_value = map(int, input().split())
c = False
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                break
        else:
            if str(number) == str(number)[::-1]:
                c = True
                print(number, end=' ')
if not c:
    print(0)
