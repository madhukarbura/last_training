days=list(map(int,input().split()))
profits=list(map(int,input().split()))
for i in range(len(profits)):
    for j in range(len(profits)-i-1):
        if profits[j]<profits[j+1]:
            #corresponding sort to list1,list2
            profits[j],profits[j+1]=profits[j+1],profits[j]
            days[j],days[j+1]=days[j+1],days[j]
ans=days[0]

for i in range(1,len(days)):
    if days[i]> ans:
        ans =days[i]
        
vis=[-1 for i in range(ans+1)]
i=0
cnt=0
while cnt<ans and i<len(profits):
    if vis[days[i]]==-1:
        vis[days[i]]=1
        cnt+=1
    else:
        for j in range(days[i]-1,0,-1):
            if vis[days[j]]==-1:
                vis[days[j]]=1
                cnt+=1
                break
    i+=1
print(cnt)