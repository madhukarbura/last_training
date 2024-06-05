n = int(input("no of elemnts:"))
arr = list(map(int,input("enter the elements").split()))
flag = 0
for i in range(0,n,2):
    if arr[i] != arr[i+1]:
        flag = 1
        break
if flag == 1:
    even=0
    for i in range(0,n,):
        if arr[i]%2==0:
            even +=1
    print(even)
else:
    odd = 0
    for i in range(0,n):
        if arr[i]%2 !=0:
            odd +=1
    print(odd)