n=int(input())
e=int(input())
parent=[i for i in range(n+1)]
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
adj=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(e):
    sv=int(input())
    ev=int(input())
    wv=int(input())
    union(sv,ev)
    adj[sv][ev]=wv
    adj[ev][sv]=wv

    