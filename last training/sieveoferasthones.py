n = int(input())
count = 0
if n < 2:
    print(0)
else:
    prime = [1 for i in range(n)]
    prime[0] = 0
    prime[1] = 0
    i = 2
    while i*i <= n:
        if prime[i] == 1:
            for j in range(2*i,n,i):
                prime[j] = 0
        i += 1
    for i in range(2,n):
        if prime[i] == 1:
            count += 1
print(count)
