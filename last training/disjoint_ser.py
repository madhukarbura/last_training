v=int(input())
e=int(input())
parent=[i for i in range(v)]
def find(a):
    if parent[a]==a:
        return a
    else:
        while parent[a]!=a:
            a=parent[a]
    return a

def union(a,b):
    x=find(a)
    y=find(b)
    if x < y:
        parent[y]=x
    else:
        parent[x]=y
for i in range(e):
    sv=int(input())
    ev=int(input())
    union(sv,ev)
ans=find(0)
flag=0
for i in range(v):
    temp=find(i)
    if temp!=ans:
        flag=1
        break
if flag==0:
    print("connected")
else:
    print("not connected")
    
    