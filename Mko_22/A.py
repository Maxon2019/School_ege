a = int(input())
b = int(input())
c = int(input())
k = int(input())

print(a // k + b // k + c // k + int(a % k != 0) + int(b % k != 0) + int(c % k != 0))
