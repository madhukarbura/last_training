arr = list(map(int, input().split()))
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a*b)/(gcd(a,b))
flag = 0
for i in range(len(arr)-1):
    arr[i+1] = lcm(arr[i],arr[i+1])
print(arr[len(arr)-1])
