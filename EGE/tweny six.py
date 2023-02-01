f = open('24.txt','r')

f = f.readline().lower()
f = f.replace('xyz',' ')
f = f.split()
f.sort(key=len)
#v = max(f,key=len)
print(len(f[-1]))
