"""n = int(input())

mat = [0] * n

sum_str = [0] * n
sum_sto = [0] * n
for i in range(n):
    mat[i] = list(map(int, input().split()))
    sum_str[i] = sum(mat[i])
print(mat,'\n',sum_str)

for j in range(n):
    for k in range(n):
        sum_sto[j] += mat[k][j]
print(sum_sto)

for m in range(n):
    for n in range()"""