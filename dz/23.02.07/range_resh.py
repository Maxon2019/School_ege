lower_value, upper_value = map(int, input().split())
t = False
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, int(number**0.5)+1):
            if (number % i) == 0:
                break
        else:
            t = True
            print(number, end=' ')
if not t:
    print(0)