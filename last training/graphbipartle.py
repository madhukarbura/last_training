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

adj=[[] for i in range(v)]
for i in range(0,e):
    sv = int(input())
    ev = int(input())
    adj[sv].append(ev)
    adj[ev].append(sv)
    
for i in range(v):
    size=len(adj[0])
    root=adj[i][0]
    for j in range(size):
        union(adj[i][j],root)
    x=find(i)
    y= find(root)
    if x==y:
        flag=1
        break
    
    
    