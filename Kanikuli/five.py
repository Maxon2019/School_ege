def f(n, s):
    if s % 2 == 0:
        n += '0'
        return n
    else:
        n += '1'
        return n


for i in range(17, 10000):
    num = list(map(int, list(str(i))))
    b = bin(i)[2:]
    su = sum(num)
    for j in range(3):
        b = f(b, su)
        num = int(b, base=2)
        num = list(map(int, list(str(num))))
        su = sum(num)
    print(int(b,base=2) )
    if int(b,base=2) > 1028:
        print(int(b,base=2))
        break
