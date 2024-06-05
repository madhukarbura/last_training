"""arr=list(map(int,input().split()))
arr1=[]
for num in arr:
    if num not in arr1:
        arr1.append(num)
print(arr1)"""
def singel_value(arr):
    pos=0
    ans=0
    for i in range(len(arr)):
        ans=ans^arr[i]
    while ans>0:
        if ans%2!=0:
            break
        pos+=1
        ans=ans//2
    temp=1<<pos
    left,right=0,0
    for i in range(len(arr)):
        if arr[i]& temp==0:
            left=left^arr[i]
            
        else:
            right=right^arr[i]
    return left,right
arr=list(map(int,input().split()))
result=singel_value(arr)
print(result)