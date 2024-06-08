n=int(input())
arr=list(map(int,input().split()))
flag=0
count=0
for i in range(n):
    for j in range(1,arr[i]+1):
        if arr[i]%j==0:
            flag+=1
        
    if flag==2:
        count+=1
arr.sort()
if count%2==0:
    print(arr[-2])
else:
    print(arr[1])
            
        