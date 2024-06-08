n=int(input())
m=int(input())
rem=n-m
rem=rem+1
max=(rem*(rem-1))//2
rem1=n//m

if n%m==0:
    min=((rem1*(rem1-1))//2)*m
    print(min)
else:
    mod=n%m
    first=rem1+1
    teams=mod
    min=((first*(first-1))//2)*teams
    second=rem1
    teams=m-mod
    min1=((second*(second-1))//2)*teams
    print(min+min1)
print(max)