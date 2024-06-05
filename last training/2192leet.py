v=int(input())
e=int(input())
adj=[[0 for i in range(v)] for j in range(v)]
for i in range(e):
    sv=int(input())
    ev=int(input())
    adj[sv][ev]=1
    adj[ev][sv]=1
 