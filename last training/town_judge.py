n=int(input())
m=int(input())
ar=[]
for i in range(m):
    temp=[]
    sv=int(input())
    ev=int(input())
    temp.append(sv)
    temp.append(ev)
    ar.append(temp)
indegre=[0 for i in range(n+1)]
outdegree=[0 for i in range(n+1)]
for i in range(m):
    sv=ar[i][0]
    ev=ar[i][1]
    indegre[ev]+=1
    outdegree[sv]+=1
flag=0
for i in range(1,n+1):
    if indegre[i]==n-1 and outdegree[i]==0:
        flag=i
        break
if flag==0:
    print("-1")
else:
    print(flag)