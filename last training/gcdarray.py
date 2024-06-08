arr = list(map(int, input().split()))
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
flag = 0
for i in range(len(arr)-1):
    arr[i+1] = gcd(arr[i],arr[i+1])
    if arr[i+1] == 1:
        flag = i+1
        break
if flag != 0:
    print(arr[flag])
else:
    print(arr[len(arr)-1])
