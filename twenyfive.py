"""for i in range(9753129):
    if 3123*i > 123405:
        print(3123*i)
    elif 3123*i > 10**9:
        break
"""
c = 0
for k in range(10):
    for n in range(10):
        if int(f'1263{k}5{n}') % 3123 ==0:
            c+=1

for i in range(1000):
    for k in range(10):
        for n in range(10):
            if int(f'12{i}63{k}5{n}') % 3123 == 0 and int(f'12{i}63{k}5{n}') < 10**9:
                c += 1
                print(f'12{i}63{k}5{n}')
print(c)