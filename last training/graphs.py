v=int(input())
e=int(input())
adj=[[0 for i in range(v)] for j in range(v)]
for i in range(e):
    sv=int(input())
    ev=int(input())
    adj[sv][ev]=1
    adj[ev][sv]=1
def bfs(adj,v,sv):
    vis=[0 for i in range(v)]
    queue=[]
    queue.append(sv)
    vis[sv]=1
    while(len(queue)>0):
        front=queue.pop(0)
        print(front,end=' ') 
        for i in range(v):
            if adj[front][i]==1 and vis[i]==0:
                queue.append(i)
                vis[i]=1
               
bfs(adj,v,0)        