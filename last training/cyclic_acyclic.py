v = int(input())
e = int(input())
def topo(adj,v,counter):
    indegree = [0 for i in range(v)]
    for i in range(0,v):
        for j in range(0,v):
            if adj[i][j] == 1:
                indegree[j] += 1
    queue = []
    for i in range(0,v):
        if indegree[i] == 0:
            queue.append(i)
    while len(queue) > 0:
        front = queue.pop(0)
        counter += 1
        for i in range(0,v):
            if adj[front][i] == 1:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
    return counter
adj = [[0 for j in range(v)] for i in range(v)]
for i in range(e):
    sv = int(input())
    ev = int(input())
    adj[sv][ev] = 1
if topo(adj,v,0) == v:
    print("Acyclic")
else:
    print("cyclic")