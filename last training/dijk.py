v = int(input())
e = int(input())
def dijk(adj,v,sv):
    dis = [1234567 for i in range(v)]
    dis[sv] = 0
    vis = [0 for i in range(v)]
    for i in range(v):
        min = 109876
        index = -1
        for j in range(v):
            if dis[j] < min:
                min = dis[j]
                index = j
        for j in range(v):
            if adj[index][j] != 0 and vis[j] == 0:
                curr = min + adj[index][j]
                if curr < dis[j]:
                    dis[j] = curr
        print(dis)
adj = [[0 for j in range(v)] for i in range(v)]
for i in range(e):
    arr = list(map(int, input().split()))
    sv = arr[0]
    ev = arr[1]
    weight = arr[2]
    adj[sv][ev] = weight
    adj[ev][sv] = weight
dijk(adj,v,0)