n = int(input())
k = int(input())
if k == 1:
    print(1)
else:
    count = 2
    j = 2
    while j <= n:
        if n % j == 0:
            if count == k:
                print(j)
                break
            count += 1
        j += 1