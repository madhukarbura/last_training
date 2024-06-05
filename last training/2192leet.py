v = int(input())
e = int(input())
adj = [[0 for j in range(v)] for i in range(v)]
revadj = [[0 for j in range(v)] for i in range(v)]
for i in range(e):
    sv = int(input())
    ev = int(input())
    adj[sv][ev] = 1
    revadj[ev][sv] = 1
def bfs(adj,v,sv,l):
    visited = [0 for i in range(v)]
    queue = []
    queue.append(sv)
    visited[sv] = 1
    while len(queue) > 0:
        front = queue.pop(0)
        l.append(front)
        for i in range(0,v):
            if adj[front][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    return l
res = []
for i in range(v):
    temp = bfs(revadj,v,i,[])
    temp.pop(0)
    temp.sort()
    res.append(temp)
print(res)