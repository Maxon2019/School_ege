c = 0

for a in range(0,97):
    for b in range(0,97):
        if (a**2 % 97) > (b**2 % 97):
            c+=1
print(c)