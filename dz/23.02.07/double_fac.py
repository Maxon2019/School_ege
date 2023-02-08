n = int(input())

factorial = 1
while n > 1:
    factorial *= n
    n -= 2

print(factorial)