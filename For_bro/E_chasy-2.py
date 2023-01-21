n = int(input())  # enter mins
n %= 86400  # check how much
ch = n // 3600  # h
m = 0
s = 0

if n - ch * 3600 > 60: # if we have mins
    m = (n - ch * 3600) // 60  # m
    s = n - m * 60 - ch * 3600  # s
else:
    s = n - ch * 3600

if m < 10:
    if s < 10:
        print(f'{ch}:0{m}:0{s}')  # print with format 00
    else:
        print(f'{ch}:0{m}:{s}')  # print with format 0
else:
    print(f'{ch}:{m}:{s}')  # print with format
