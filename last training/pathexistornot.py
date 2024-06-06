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

flag=0
x=int(input())
y=int(input())
ans=find(x)
ans2=find(y)
if ans!=ans2:
    print("path not exist")
else:
    print("path exist")

    
    