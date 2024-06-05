arr=list(map(int,input().split()))
ans=0
for i in range(len(arr)):
    ans=ans^arr[i]
print(ans)