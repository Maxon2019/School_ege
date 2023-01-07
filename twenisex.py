f = open('26.txt', 'r')
f = f.readlines()
cubes = []

for i in range(len(f)):
    f[i] = f[i].split()
    cubes.append([int(f[i][0]), f[i][1]])

cubes = sorted(cubes)[::-1]

skladovsk = []

while len(cubes) > 0:
    fat_block = [cubes.pop(0)]
    for i in range(len(cubes)):
        if cubes[i][1] != fat_block[-1][1] and fat_block[-1][0] - cubes[i][0] >= 5:
            fat_block.append(cubes[i])
            cubes[i] = ''
    cubes = [x for x in cubes if x != '']
    skladovsk.append(len(fat_block))

print(max(skladovsk),len(skladovsk))
