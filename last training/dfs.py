v = int(input())
e = int(input())
adj = [[0 for j in range(v)] for i in range(v)]
#revadj = [[0 for j in range(v)] for i in range(v)]
for i in range(e):
    sv = int(input())
    ev = int(input())
    adj[ev][sv] = 1
    adj[sv][ev]=1
vis=[0 for i in range(v)]
def dfs(adj,v,sv,vis):
    vis[sv]=1
    print(sv,end=" ")
    for i in range(v):
        if adj[sv][i]==1 and vis[i]==0:
            dfs(adj,v,i,vis)
dfs(adj,v,0,vis)