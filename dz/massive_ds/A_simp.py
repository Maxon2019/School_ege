with open('input.txt','r') as fout, open('output.txt','w') as fin:
    an = int(fout.readline())
    l = []
    while an !=0:
        l.append(an)
        an = int(fout.readline())
    l.sort()
    l = [str(i) for i in l]
    fin.write(f"{' '.join(l)}")