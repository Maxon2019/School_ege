n = int(input())  # enter mins
n %= 1440  # check how much
ch = n // 60  # h
m = n - ch * 60  # m
print(ch, m)  # print
