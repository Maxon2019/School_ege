'''c = 0

for x in range(100, 1000):
    for y in range(10000, 100000):
        if 2090910 <= 9091 * x + 91 * y <= 2090921:
            c += 1
            print(x,y)
print(c)'''
n = int(input()) # промежуток [n;m]
m = int(input())
a = []
print("sum : num : new_num")
for i in range (10000000, m+1):
    num = str(i)
    if num[3] != "0":
        new_num = num[3:] + num[:3]
        sum = (int(num) + int(new_num))
        if (sum <= m) and (sum >= n):
            print(str(sum) + " : " + num + " : " + new_num)
            if sum not in a:
                a.append(sum)
print("Total: " + str(len(a)))