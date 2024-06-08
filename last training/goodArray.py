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
        flag = 1
        break
if flag == 1:
    print("True")
else:
    print("False")
