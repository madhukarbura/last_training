n = int(input())
ar = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        temp = int(input())
        ar[i][j] = temp
def prime(x):
    if x < 2:
        return 0
    flag = 0
    for i in range(2,x//2):
        if x % i == 0:
            return 0
    return 1
count = 0
for i in range(n):
    for j in range(n):
        if i == j:
            if prime(ar[i][j]):
                count += 1
print(count) 