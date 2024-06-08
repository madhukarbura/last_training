n = int(input())
count = 0
for j in range(2,n):
    i = 2
    flag = 0
    while i <= j//2 :
        if j % i == 0:
            flag = 1
            break
        i += 1
    if flag == 0:
        count += 1
print(count)