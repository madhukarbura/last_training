v = int(input())
e = int(input())
adj=[[] for i in range(v)]
for i in range(0,e):
    sv = int(input())
    ev = int(input())
    adj[sv].append(ev)
    adj[ev].append(sv)
print(adj)