n,t=map(int,input().split())
if n==1 and t==10:
    print(-1)
else:
    s=''
    if t!=10:
        s=str(t)*n
    else:
        s='1'+'0'*(n-1)
    print(s)