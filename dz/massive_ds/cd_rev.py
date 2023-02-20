with open('input.txt', 'r') as fout, open('output.txt', 'w') as fin:
    an = int(fout.readline())
    l = []
    while an != 0:
        l.append(an)
        an = int(fout.readline())
    ll = len(l) // 2
    l1 = l[:ll:]
    l2 = l[ll::]
    l1, l2 = l1[::-1], l2[::-1]
    l1 = [str(i) for i in l1]
    l2 = [str(i) for i in l2]
    l = ' '.join(l1) + ' ' + ' '.join(l2)
    fin.write(f"{l}")
