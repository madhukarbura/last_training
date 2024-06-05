def fibb(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)
num=int(input("enter the number: "))
ans=fibb(num)
print(ans)