s = open('24.txt', 'r')

s = str(s.readlines()[0])
s = s.replace('F', '4')
s = s.replace('A', '1')
s = s.replace('C', '_')
s = s.replace('D', '_')
s = s.replace('O', '_')
print(s)

mfs_counter = 0
state_f = 0
state_a = 0
max_d = -1
c = 0
while c < len(s):
    if s[c] == '4' and state_f == 0:
        ind1 = 0
        mfs_counter += 1
        state_f += 1
    elif s[c] == '4' and state_f == 1:
        state_f = 0

